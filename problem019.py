#!/usr/bin/env python3

from itertools import *

def dates(year, month, day):

    def is_leap_year(year):
        return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

    def days_per_month(year, month):
        if month == 2:
            return 29 if is_leap_year(year) else 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    while True:
        yield (year, month, day)
        day += 1
        if day > days_per_month(year, month):
            day = 1
            month += 1
            if month > 12:
                month = 1
                year += 1

sundays = islice(dates(1900, 1, 7), 0, None, 7)
sundays = dropwhile(lambda date: date < (1901, 1, 1), sundays)
sundays = takewhile(lambda date: date <= (2000, 12, 31), sundays)
print(sum(1 for (year, month, day) in sundays if day == 1))
