#!/usr/bin/env python3

from itertools import *

def nth(iterable, n):
    return next(islice(iterable, n - 1, None))

print(''.join(nth(permutations('0123456789'), 1000000)))
