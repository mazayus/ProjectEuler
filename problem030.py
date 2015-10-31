#!/usr/bin/env python3

from itertools import *

def digits(number):
    yield from map(int, str(number))

maxpower = next(dropwhile(lambda n: n * 9**5 > 10**n, count(1)))
print(sum(n for n in range(2, 10**maxpower+1)
          if n == sum(d**5 for d in digits(n))))
