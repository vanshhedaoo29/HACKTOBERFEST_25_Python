def interpolationSearch(arr, low, high, x):
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    if (low <= high and x >= arr[low] and x <= arr[high]):
        if arr[high] == arr[low]:
            return low if arr[low] == x else -1

        # Probing the position with keeping
        # uniform distribution in mind.
        pos = low + ((high - low) // (arr[high] - arr[low]) * (x - arr[low]))

        # This guard is defensive; for the integer formula and the
        # outer if-condition pos will always be inside [low, high].
        # Mark as no cover to avoid unreachable-code coverage failures.
        if pos < low or pos > high:
            return -1  # pragma: no cover

        # Condition of target found
        if arr[pos] == x:
            return pos
        # If x is larger, x is in right subarray
        elif arr[pos] < x:
            return interpolationSearch(arr, pos + 1, high, x)
        # If x is smaller, x is in left subarray
        else:
            return interpolationSearch(arr, low, pos - 1, x)

    return -1

  
if __name__ == "__main__":  # pragma: no cover
    arr = [10, 12, 13, 16, 18, 19, 20, 21,
           22, 23, 24, 33, 35, 42, 47]
    x = 18
    index = interpolationSearch(arr, 0, len(arr) - 1, x)
    if index != -1:
        print("Element found at index", index)
    else:
        print("Element not found")
        
