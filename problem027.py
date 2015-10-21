#!/usr/bin/env python3

from functools import *
from itertools import *
import operator

@lru_cache(maxsize=None)
def is_prime(number):
    if number <= 0:
        return False
    for d in range(2, round(number**0.5) + 1):
        if number % d == 0:
            return False
    return True

def num_quad_primes(a, b):
    return len(list(takewhile(is_prime, ((n+a)*n+b for n in count(0)))))

def product(sequence):
    return reduce(operator.mul, sequence)

coeffs = ((a, b)
          # n = 0 => n^2 + a*n + b = b => b is prime
          for b in range(2, 1000) if is_prime(b)
           # n = 1 => n^2 + a*n + b = a+b+1 => a+b+1 is prime
          for a in range(-b, 1000) if is_prime(a+b+1))

print(product(max(coeffs, key=lambda pair: num_quad_primes(*pair))))
