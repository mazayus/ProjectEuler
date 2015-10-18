#!/usr/bin/env python3

from functools import *
import operator

def factorial(number):
    assert number >= 1
    return reduce(operator.mul, range(1, number+1))

def digits(number):
    yield from (int(digit) for digit in str(number))

print(sum(digits(factorial(100))))
