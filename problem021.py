#!/usr/bin/env python3

from functools import *
from itertools import *

def divisors(n):
    for d in takewhile(lambda d: d * d <= n, count(1)):
        if n % d == 0:
            yield d
            if n // d != d:
                yield n // d

@lru_cache(maxsize=None)
def sum_proper_divisors(n):
    return sum(divisors(n)) - n

@lru_cache(maxsize=None)
def is_amicable_number(n):
    sumdivs = sum_proper_divisors(n)
    return n != sumdivs and n == sum_proper_divisors(sumdivs)

print(sum(filter(is_amicable_number, range(1, 10000))))
