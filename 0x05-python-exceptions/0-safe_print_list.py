def safe_print_list(my_list=[], x=0):
    """
    Safely prints the first x elements of a list.

    Args:
        my_list: The list to print elements from.
        x (int): The number of elements to print. Defaults to 0.

    Returns:
        int: The real number of printed elements.
    """
    elements_printed = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elements_printed += 1
        except IndexError:
            break

    print("")
    return elements_printed
