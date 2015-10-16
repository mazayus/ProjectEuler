#!/usr/bin/env python3

from functools import *

@lru_cache(maxsize=None)
def latticepaths(i, j):
    if i < 0 or j < 0:
        return 0
    if i == 0 or j == 0:
        return 1
    return latticepaths(i-1, j) + latticepaths(i, j-1)

print(latticepaths(20, 20))
