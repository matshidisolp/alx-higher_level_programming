#!/usr/bin/python3

def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False


# Call the function and print the result
char_to_check = 'a'
result = islower(char_to_check)
print(result)
