#!/usr/bin/env python3

def factors(number):
    factor = 2
    while number > 1:
        while number % factor == 0:
            yield factor
            number /= factor
        factor += 1

def last(iterable):
    for value in iterable:
        pass
    return value

print(last(factors(600851475143)))
