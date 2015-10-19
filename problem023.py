#!/usr/bin/env python3

from itertools import *

def divisors(n):
    for d in takewhile(lambda d: d * d <= n, count(1)):
        if n % d == 0:
            yield d
            if n // d != d:
                yield n // d

def is_abundant_number(n):
    return n < sum(divisors(n)) - n

all_abundant = set(filter(is_abundant_number, range(1, 28123+1)))
print(sum(n for n in range(1, 28123+1)
          if not any(n-d in all_abundant for d in all_abundant)))
