#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

digit = abs(number) % 10

if number < 0:
    digit = -digit

if digit > 5:
    comparison_result = "greater than 5"
elif digit == 0:
    comparison_result = "0"
else:
    comparison_result = "less than 6 and not 0"
print("Last digit of {} is {} and is {}"
      .format(number, digit, comparison_result), end="\n")
