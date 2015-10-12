#!/usr/bin/env python3

from functools import *

def gcd(a, b):
    assert a >= 0 and b >= 0
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(reduce(lcm, range(1, 21)))
