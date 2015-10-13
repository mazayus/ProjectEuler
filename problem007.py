#!/usr/bin/env python3

from itertools import *

def primes():
    allprimes = []

    def isprime(n):
        for p in takewhile(lambda p: p * p <= n, allprimes):
            if n % p == 0:
                return False
        return True

    for n in count(2):
        if isprime(n):
            yield n
            allprimes.append(n)

def nth(iterable, n):
    return next(islice(iterable, n - 1, None))

print(nth(primes(), 10001))
