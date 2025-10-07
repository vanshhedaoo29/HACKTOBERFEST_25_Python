def interpolationSearch(arr, n, x):
    """
    Interpolation Search Algorithm.
    Works on sorted arrays of numeric values.
    Returns index of x if found, else -1.
    """

    # Ensure numeric array
    if n == 0:
        return -1
    if not all(isinstance(i, (int, float)) for i in arr):
        # Strings or mixed types not supported
        return -1

    low = 0
    high = n - 1

    while low <= high and x >= arr[low] and x <= arr[high]:

        # Single element case
        if low == high:
            return low if arr[low] == x else -1

        # Avoid division by zero if all elements in range are equal
        if arr[high] == arr[low]:
            return low if arr[low] == x else -1

        # Calculate probe position
        pos = int(low + ((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))

        # Safety: clamp pos within array bounds
        pos = max(low, min(pos, high))

        if arr[pos] == x:
            # Find first occurrence if duplicates exist
            while pos > 0 and arr[pos - 1] == x:
                pos -= 1
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1


if __name__ == "__main__":  # pragma: no cover
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    n = len(arr)
    x = 18
    index = interpolationSearch(arr, n, x)
    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found")
