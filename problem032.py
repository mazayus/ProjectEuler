#!/usr/bin/env python3

from itertools import *

def pandigital_products():
    for i in count(1):
        if '0' in str(i):
            continue
        iistr = str(i) + str(i) + str(i*i)
        if len(iistr) > 9:
            break
        for j in count(i+1):
            if '0' in str(j):
                continue
            ijstr = str(i) + str(j) + str(i*j)
            if len(ijstr) > 9:
                break
            if ''.join(sorted(ijstr)) == '123456789':
                yield i*j

print(sum(set(pandigital_products())))
