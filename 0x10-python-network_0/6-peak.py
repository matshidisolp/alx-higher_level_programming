def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    def binary_search(arr, left, right):
        mid = (left + right) // 2

        if (mid == 0 or arr[mid] >= arr[mid - 1]) and \
           (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
            return arr[mid]

        if mid > 0 and arr[mid] < arr[mid - 1]:
            return binary_search(arr, left, mid - 1)

        return binary_search(arr, mid + 1, right)

    return binary_search(list_of_integers, 0, len(list_of_integers) - 1)
