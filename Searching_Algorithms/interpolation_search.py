def interpolationSearch(arr, n, x):
    """
    Interpolation Search Algorithm.
    Works on sorted arrays of numeric values.
    Returns index of the first occurrence of x if found, else -1.
    """

    # Ensure array has numeric types and x is numeric
    if not arr or not all(isinstance(e, (int, float)) for e in arr) or not isinstance(x, (int, float)):
        return -1

    low = 0
    high = n - 1
    result = -1  # Track first occurrence

    while low <= high and x >= arr[low] and x <= arr[high]:

        if arr[high] == arr[low]:
            if arr[low] == x:
                return low
            else:
                return -1

        pos = low + int((float(high - low) / (arr[high] - arr[low])) * (x - arr[low]))

        if arr[pos] == x:
            result = pos
            # continue search in the lower part for earlier occurrence
            high = pos - 1
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return result


if __name__ == "__main__":  # pragma: no cover
    arr = [10, 12, 13, 16, 18, 19, 20, 21,
           22, 23, 24, 33, 35, 42, 47]
    n = len(arr)
    x = 18
    index = interpolationSearch(arr, n, x)

    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found")
