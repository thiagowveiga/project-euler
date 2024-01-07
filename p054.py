class Card:
    def __init__(self, card):   # card is a string of 2 chrs such as '4C'
        if ord(card[0]) >= 50 and ord(card[0]) <= 57:
            self.rank = int(card[0])
        elif card[0] == 'T':
            self.rank = 10
        elif card[0] == 'J':
            self.rank = 11
        elif card[0] == 'Q':
            self.rank = 12
        elif card[0] == 'K':
            self.rank = 13
        elif card[0] == 'A':
            self.rank = 14
        
        if card[1] == 'C':
            self.suit = 'Clubs'
        if card[1] == 'D':
            self.suit = 'Diamonds'
        if card[1] == 'H':
            self.suit = 'Hearts'
        if card[1] == 'S':
            self.suit = 'Spades'

class Hand:
    def __init__(self, hand): # hand is a list of 5 Cards

        one_pair = False
        two_pairs = False
        three_of_a_kind = False
        straight = False
        flush = False
        full_house = False
        four_of_a_kind = False
        straight_flush = False
        royal_flush = False

        # repeated card values
        self.all_cards_values = []
        unique_ranks = set()
        pairs = set()  # values for which theres a pair
        three = set()  # value for which theres a "three of a kind"
        four = set()  # value for which theres a "four of a kind"
        for card in hand:
            if card.rank in unique_ranks:
                if card.rank in pairs:
                    if card.rank in three:
                        four.add(card.rank)
                    three.add(card.rank)
                pairs.add(card.rank)
            unique_ranks.add(card.rank)
            self.all_cards_values.append(card.rank)
        self.all_cards_values.sort()

        if len(pairs):
            one_pair = True
            if len(pairs) >= 2:
                two_pairs = True
                two_pairs_values = [min(pairs), max(pairs)]
        
        if len(three):
            three_of_a_kind = True
            if two_pairs:
                full_house = True

        if len(four):
            four_of_a_kind = True

        # -------------------------------------------------------

        # straight
        check_consec = list(unique_ranks)
        check_consec.sort
        if len(check_consec) != 5:
            straight = False
        elif (14 in check_consec) and (2 in check_consec) and (3 in check_consec) and (4 in check_consec) and (5 in check_consec):
            straight = True
        else:
            straight = True
            for i in range(1, 5):
                if check_consec[i] != (check_consec[i-1]+1):
                    straight = False
        if straight:
            last = check_consec[-1]
        # -------------------------------------------------------

        # flush
        unique_suits = set()
        flush_values = []
        for card in hand:
            if card.suit not in unique_suits:
                unique_suits.add(card.suit)
        if len(unique_suits) == 1:
            flush = True
            for card in hand:
                if card.suit == list(unique_suits)[0]:
                    flush_values.append(card.rank)
            flush_values.sort()
        # -------------------------------------------------------

        # straight and royal flush
        if straight and flush:
            straight_flush = True
            if last == 14:
                royal_flush = True
        # -------------------------------------------------------

        if royal_flush:
            self.hand_rank = 9
            self.tie_breaker = self.all_cards_values
        elif straight_flush:
            self.hand_rank = 8
            self.tie_breaker = last
        elif four_of_a_kind:
            self.hand_rank = 7
            self.tie_breaker = list(four)[0]
        elif full_house:
            self.hand_rank = 6
            self.tie_breaker = list(three)[0]
        elif flush:
            self.hand_rank = 5
            self.tie_breaker = flush_values
        elif straight:
            self.hand_rank = 4
            self.tie_breaker = last
        elif three_of_a_kind:
            self.hand_rank = 3
            self.tie_breaker = list(three)[0]
        elif two_pairs:
            self.hand_rank = 2
            self.tie_breaker = two_pairs_values
        elif one_pair:
            self.hand_rank = 1
            self.tie_breaker = list(pairs)[0]
        else:
            self.hand_rank = 0
            self.tie_breaker = self.all_cards_values   # the player has only a "high card"
        # -------------------------------------------------------

def greater_same_rank(h1, h2):  # two hands (of the same rank) are passed, the greatest is returned
    rank = h1.hand_rank
    def compare_lists(l1, l2):
        for i in range(-1, (-1*len(l1))-1, -1):
            if l2[i] > l1[i]:
                return 2
            elif l1[i] > l2[i]:
                return 1
        return 'tie'
    if (rank == 0) or (rank == 2) or (rank == 5) or (rank == 9):
        greater = compare_lists(h1.tie_breaker, h2.tie_breaker)
        if greater != 'tie':
            return greater
        else:
            return compare_lists(h1.all_cards_values, h2.all_cards_values)
    else:
        if h1.tie_breaker > h2.tie_breaker:
            return 1
        elif h1.tie_breaker < h2.tie_breaker:
            return 2
        else:
            return compare_lists(h1.all_cards_values, h2.all_cards_values)
wins1 = 0
wins2 = 0
    
with open('files/p054.txt') as hands:
    for hand in hands:
        p1 = hand.split()[0:5]
        p2 = hand.split()[5:10]
        for i in range(5):
            p1[i] = Card(p1[i])
            p2[i] = Card(p2[i])

        p1 = Hand(p1)
        p2 = Hand(p2)

        if p1.hand_rank > p2.hand_rank:
            wins1 += 1
        elif p1.hand_rank < p2.hand_rank:
            wins2 += 1
        elif p1.hand_rank == p2.hand_rank:
            winner = greater_same_rank(p1, p2)
            if winner == 1:
                wins1 += 1
            else:
                wins2 += 1

print(f'Player 1 wins {wins1} hands, while player 2 wins {wins2} hands!')