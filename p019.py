# How many Sundays fell on the first of the month during the 
# twentieth century (1 Jan 1901 to 31 Dec 2000)?

days_in_month = {
    1  : 31,
    2  : 28,
    3  : 31,
    4  : 30,
    5  : 31,
    6  : 30,
    7  : 31,
    8  : 31,
    9  : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

year_count = 1901

cont_days = 1   # counts days continuously w no regard for month or year

count_until = 2000  #included

target = 0

while year_count <= count_until:
    month_count = 1
    if (year_count % 4 == 0  and not year_count % 100 == 0) or (year_count % 400 == 0):
        leap = True
    else:
        leap = False
    while month_count <= 12:
        max_days = days_in_month[month_count]
        if (max_days == 28) and (leap):
            max_days += 1
        day_count = 1
        while day_count <= max_days:
            weekday = cont_days % 7
            if (day_count == 1) and (weekday == 6):
                target += 1
            day_count += 1
            cont_days += 1  
        month_count += 1
    year_count += 1

print(target)