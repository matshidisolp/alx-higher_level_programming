def safe_print_list(my_list=[], x=0):
    """
    Safely prints the first x elements of a list.

    Args:
        my_list: The list to print elements from.
        x (int): The number of elements to print. Defaults to 0.

    Returns:
        int: The number of printed elements.
    """

    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
