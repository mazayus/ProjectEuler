#!/usr/bin/env python3

NUMBER_TO_STRING = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

def number_to_string(number):
    assert number >= 0 and number < 1000000

    if number == 0:
        return None

    thousands = number_to_string(number // 1000)
    number = number % 1000
    if thousands:
        remainder = number_to_string(number)
        if remainder:
            return thousands + " thousand and " + remainder
        else:
            return thousands + " thousand"

    hundreds = number_to_string(number // 100)
    number = number % 100
    if hundreds:
        remainder = number_to_string(number)
        if remainder:
            return hundreds + " hundred and " + remainder
        else:
            return hundreds + " hundred"

    if number in NUMBER_TO_STRING:
        return NUMBER_TO_STRING[number]

    tens, ones = number // 10, number % 10
    return NUMBER_TO_STRING[tens * 10] + " " + NUMBER_TO_STRING[ones]

print(sum(len(number_to_string(n).replace(' ', '')) for n in range(1, 1001)))
