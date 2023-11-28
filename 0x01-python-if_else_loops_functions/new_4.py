#!/usr/bin/python3

"""Print numbers 0 to 98 in decimal and hexadecimal."""
formatted_numbers = ["{} = {}".format(number, hex(number)) for number in range(99)]
print("\n ".join(formatted_numbers))

