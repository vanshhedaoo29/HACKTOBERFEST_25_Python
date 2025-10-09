# Returns index of x if present, else returns -1
def fibonacciSearch(arr, x):
    n = len(arr)

    if n == 0:
        return -1 

    # initialize first three fibonacci numbers
    a =  0
    b = 1
    c = 1
 
    # iterate while c is smaller than n
    # c stores the smallest Fibonacci 
    # number greater than or equal to n
    while c < n:
        a = b
        b = c
        c = a + b
 
    # marks the eliminated range from front
    offset = -1
 
    # while there are elements to be inspected
    # Note that we compare arr[a] with x. 
    # When c becomes 1, a becomes 08
    while c > 1:

        # check if a is a valid location
        i = min(offset + a, n - 1)
 
        # if x is greater than the value at index a,
        # cut the subarray array from offset to i 
        if arr[i] < x:
            c = b
            b = a
            a = c - b
            offset = i
 
        # else if x is greater than the value at 
        # index a,cut the subarray after i+1
        elif arr[i] > x:
            c = a
            b = b - a
            a = c - b
 
        # else if element found, return index
        else:
            return i
 
    # comparing the last element with x
    if b and arr[offset + 1] == x:
        return offset + 1
 
    # element not found, return -1
    return -1


if __name__ == "__main__": # pragma: no cover
    arr = [2, 3, 4, 10, 40]
    x = 10
    print(fibonacciSearch(arr, x))
