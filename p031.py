# How many different ways can £2 be made using any number of coins?

# I was going kinda in the right direction but then gave up and looked for help:
# this page helped a lot https://algorithmist.com/wiki/Coin_change

def problem(amount, coins):     # N and S in the link above

    sum_ = 0

    if amount < 0:  # exceeded the target amount
        return 0
    if not coins:   # used all the coins avaiable (only happens after there's only 1p coins to use to properly invalidate the "doesnt use the biggest coin" case)
        return 0
    if amount == 0:   # found a way to use the coins to sum to the target amount
        return 1

    # uses the biggest coin
    sum_ += problem(amount-coins[0], coins[:])

    # doesnt use the biggest coin
    sum_ += problem(amount, coins[1:])

    return sum_

print(problem(200, [200, 100, 50, 20, 10, 5, 2, 1]))