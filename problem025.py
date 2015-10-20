#!/usr/bin/env python3

def fibs():
    fib1, fib2 = 1, 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2

print(next(i for (i, f) in enumerate(fibs(), 1) if len(str(f)) == 1000))
