import math
from typing import List, Union


def jumpSearch(arr: List[Union[int, float, str]], x: Union[int, float, str], n: int) -> int:
    # Handle edge case: empty array
    if n == 0:
        return -1

    # If target is smaller than the first element, fail fast
    if arr[0] > x:
        return -1

    # Determine block size to jump
    step = int(math.sqrt(n))
    if step <= 0:
        step = 1

    # Find the block where element may exist
    prev = 0
    while prev < n:
        next_idx = min(prev + step, n) - 1
        if arr[next_idx] >= x:
            break
        prev += step
        if prev >= n:
            return -1

    # Linear search within the block
    end = min(prev + step, n)
    for i in range(prev, end):
        if arr[i] == x:
            return i

    # Final return for not found
    return -1


if __name__ == "__main__":  # pragma: no cover
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
           34, 55, 89, 144, 233, 377, 610]
    x = 55
    n = len(arr)
    index = jumpSearch(arr, x, n)
    print(f"Number {x} is at index {index}")

    # This code is contributed by "Sharad_Bhardwaj".
