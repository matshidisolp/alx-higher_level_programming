#!/usr/bin/python3

def islower(c):
    """Check for lowercase characters."""
    return ord('a') <= ord(c) <= ord('z')


# Call the function and print the result
char_to_check = 'a'
result = islower(char_to_check)
print(result)
