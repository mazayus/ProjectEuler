#!/usr/bin/env python3

def spiral_corners(size):
    yield 1

    num = 1
    sidelen = 3
    while sidelen <= size:
        for _ in range(4):
            num += sidelen - 1
            yield num
        sidelen += 2

print(sum(spiral_corners(1001)))
