#!/usr/bin/env python3

def palindromeproducts(start, stop):

    def ispalindrome(n):
        return str(n) == str(n)[::-1]

    for n1 in range(start, stop):
        for n2 in range(n1, stop):
            product = n1 * n2
            if ispalindrome(product):
                yield product

print(max(palindromeproducts(100, 1000)))
