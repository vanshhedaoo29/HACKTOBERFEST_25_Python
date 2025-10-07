import math
from typing import List, Union

def jumpSearch(arr: List[Union[int, float, str]], x: Union[int, float, str], n: int) -> int:
    # Handle edge case: empty array
    if n == 0:
        return -1

    # If target is smaller than the first element, fail fast
    # This branch is explicit and easy to test
    if n > 0 and arr[0] > x:
        return -1

    # Finding block size to be jumped (use integer step)
    step = int(math.sqrt(n))
    if step <= 0:
        step = 1

    # Finding the block where element is present (if it is present)
    prev = 0
    # Jump in integer steps, checking the element at the end of the block
    while prev < n:
        next_idx = min(prev + step, n) - 1
        # If the end-of-block element is >= x, stop jumping; target may be in this block
        if arr[next_idx] >= x:
            break
        prev += step
        # If we've advanced past array, element not present
        if prev >= n:
            return -1

    # Doing a linear search for x in block beginning with prev
    end = min(prev + step, n)
    for i in range(prev, end):
        # If we encounter an element greater than x, element is not present
        if arr[i] > x:
            return -1
        if arr[i] == x:
            return i

    # If element is not found in the block
    return -1  # Element not found

if __name__ == "__main__":  # pragma: no cover
    # Driver code to test function
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
           34, 55, 89, 144, 233, 377, 610]
    x = 55
    n = len(arr)

    # Find the index of 'x' using Jump Search
    index = jumpSearch(arr, x, n)

    # Print the index where 'x' is located
    print("Number", x, "is at index", "%.0f" % index)

    # This code is contributed by "Sharad_Bhardwaj".
