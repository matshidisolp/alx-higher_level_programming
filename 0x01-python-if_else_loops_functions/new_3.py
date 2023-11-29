#!/usr/bin/python3

# Generate a string of lowercase letters from 'a' to 'z' excluding 'q' and 'e'
letters_to_print = ''.join(chr(letter) for letter in range(97, 123) if chr(letter) not in ('q', 'e'))

# Print the resulting string
print(letters_to_print, end="")
