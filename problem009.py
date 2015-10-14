#!/usr/bin/env python3

def special_pythagorean_triplet(target_sum):
    for a in range(1, target_sum+1):
        for b in range(a+1, target_sum+1-a):
            c = target_sum - (a + b)
            if c > 0 and a*a + b*b == c*c:
                return a*b*c

print(special_pythagorean_triplet(1000))
