#!/usr/bin/env python3

def fibs(maxnumber):
    fib1, fib2 = 1, 2
    while fib1 < maxnumber:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2

print(sum(f for f in fibs(4000000) if f % 2 == 0))
