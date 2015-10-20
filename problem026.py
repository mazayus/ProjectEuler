#!/usr/bin/env python3

def period_length(denominator):
    remainders = []
    numerator = 1
    while numerator not in remainders:
        remainders.append(numerator)
        numerator = numerator * 10 % denominator
    if remainders[-1] == 0:
        return 0
    else:
        return len(remainders) - remainders.index(numerator)

print(max(range(1, 1000), key=period_length))
