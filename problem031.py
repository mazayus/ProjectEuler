#!/usr/bin/env python3

from functools import *

@lru_cache(maxsize=None)
def coinsums(target, coins):
    if target == 0:
        return 1
    if target < 0:
        return 0
    if not coins:
        return 0
    return coinsums(target - coins[0], coins) + coinsums(target, coins[1:])

print(coinsums(200, (1, 2, 5, 10, 20, 50, 100, 200)))
