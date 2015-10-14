#!/usr/bin/env python3

from functools import *
from itertools import *
import operator

def factors(number):
    factor = 2
    while number > 1:
        while number % factor == 0:
            yield factor
            number /= factor
        factor += 1

@lru_cache(maxsize=None)
def numdivisors(number):
    assert number >= 1
    factorpowers = (len(list(g)) for k, g in groupby(factors(number)))
    return reduce(operator.mul, (fp + 1 for fp in factorpowers), 1)

def highly_divisible_triangle_number(min_num_divisors):
    for n in count(1):
        if n % 2 == 0:
            n1, n2 = n // 2, n + 1
        else:
            n1, n2 = n, (n + 1) // 2
        n1div, n2div = numdivisors(n1), numdivisors(n2)
        if n1div * n2div >= min_num_divisors:
            return n1 * n2

print(highly_divisible_triangle_number(501))
