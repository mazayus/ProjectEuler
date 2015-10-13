#!/usr/bin/env python3

def sumsq(maxnumber):
    return sum(n**2 for n in range(1, maxnumber+1))

def sqsum(maxnumber):
    return sum(range(1, maxnumber+1))**2

print(sqsum(100) - sumsq(100))
