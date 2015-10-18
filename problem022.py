#!/usr/bin/env python3

def score(name):
    return sum(ord(c) - ord('a') + 1 for c in name.lower())

with open("data/problem022_names.txt", 'r') as f:
    names = sorted(name.strip('"') for name in f.read().split(','))
    print(sum(i * s for (i, s) in enumerate(map(score, names), 1)))
