#!/usr/bin/env python3

from functools import *

@lru_cache(maxsize=None)
def collatzlength(n):
    assert n >= 1
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatzlength(n // 2)
    else:
        return 1 + collatzlength(3 * n + 1)

print(max(range(1, 1000000), key=collatzlength))
