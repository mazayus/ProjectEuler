#!/usr/bin/env python3

from itertools import *

def sieve(maxprime):
    sieve = [False] * 2 + [True] * (maxprime-1)
    for p in range(2, maxprime+1):
        if not sieve[p]:
            continue
        k = 2
        while k * p <= maxprime:
            sieve[k * p] = False
            k += 1
    return sieve

print(sum(compress(range(2000000), sieve(2000000))))
