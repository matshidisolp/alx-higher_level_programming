#!/usr/bin/python3

def islower(c):
    """Check for lowercase characters."""
    return 'a' <= c <= 'z' and c.isalpha()


# Call the function and print the result
char_to_check = 'a'
result = islower(char_to_check)
print(result)
