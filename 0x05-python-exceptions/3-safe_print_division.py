#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Returns the division of a by b.

    Args:
        a: Numerator.
        b: Denominator.

    Returns:
        float or None: Result of the division or Error if None or ZeroDivision
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))

        return div
