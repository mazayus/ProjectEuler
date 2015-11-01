#!/usr/bin/env python3

from fractions import *
from functools import *
from itertools import *
import operator

def proper_fractions():
    for denom in range(10, 100):
        for numer in range(10, denom):
            yield (numer, denom)

def is_digit_cancelling(fraction):
    numer, denom = fraction
    numer10, numer1 = numer // 10, numer % 10
    denom10, denom1 = denom // 10, denom % 10

    if numer1 == 0 and denom1 == 0:
        return False

    if (numer10 == denom10 and denom1 != 0
            and Fraction(numer1, denom1) == Fraction(numer, denom)):
        return True
    if (numer10 == denom1 and denom10 != 0
            and Fraction(numer1, denom10) == Fraction(numer, denom)):
        return True
    if (numer1 == denom10 and denom1 != 0
            and Fraction(numer10, denom1) == Fraction(numer, denom)):
        return True
    if (numer1 == denom1 and denom10 != 0
            and Fraction(numer10, denom10) == Fraction(numer, denom)):
        return True

    return False

digit_cancelling_fractions = filter(is_digit_cancelling, proper_fractions())
print(reduce(operator.mul, starmap(Fraction, digit_cancelling_fractions)).denominator)
