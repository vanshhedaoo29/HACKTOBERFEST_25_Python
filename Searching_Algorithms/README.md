# Searching Algorithms

## Table Of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Testing](#testing)
  - [Running Unit Tests](#running-unit-tests)
  - [Manual Testing](#manual-testing)
- [Algorithms](#algorithms)
    - [Binary Search](#binary-search)
        - [Problem](#problem)
        - [Code](/Searching_Algorithms/binary_search.py)
    - [Fibonacci Search](/Searching_Algorithms/fibonacci_search.py)
    - [Interpolation Search](/Searching_Algorithms/interpolation_search.py)
    - [Jump Search](/Searching_Algorithms/jump_search.py)
    - [Linear Search](/Searching_Algorithms/linear_search.py)
      - [Problem](#problem-2)
      - [Code](/Searching_Algorithms/linear_search.py)


## Introduction
This project demonstrates various searching algorithms implemented in Python. It includes both classical and optimized approaches, with examples and test cases.

## Prerequisites
- Python 3.x installed
- `pip` (Python package installer) available in your environment
- Basic understanding of arrays and algorithmic logic
- Familiarity with command-line interface

## Environment Setup

To ensure a clean and isolated Python environment, it's recommended to use a virtual environment.

### Step 1: Create a Virtual Environment
```bash
python3 -m venv venv
```

### Step 2: Activate the Virtual Environment

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

- **Windows:**
  ```bash
  .\venv\Scripts\activate
  ```

### Step 3: Install Dependencies
Ensure you have a `requirements.txt` file in the root directory. Then run:
```bash
pip install -r requirements.txt
```

### Step 4: Deactivate When Done
```bash
deactivate
```

## Installation
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/A-K-0/HACKTOBERFEST_25_Python.git
cd Searching_Algorithms
```

## Configuration
No special configuration is required. All scripts are standalone and ready to run.

## Running the Application
To run any algorithm, execute the corresponding Python file:
```bash
python binary_search.py
```

## Testing

### Running Unit Tests
Unit tests are located in the `tests/` directory. Run them using:
```bash
pytest tests/
```

### Manual Testing
You can manually test each algorithm by modifying the input arrays and target values in the respective script files.

## Algorithms

### Binary Search  
**Source**: [Binary Search](https://www.geeksforgeeks.org/dsa/binary-search/)

#### Problem  
Given a **sorted array** `arr[]` of `n` integers and a target element `x`, determine whether `x` is present in the array. Return the **index** of `x` if found, or **-1** if it is not present.

> **Input**: arr[] = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], x = 23  
> **Output**: 5  
> **Explanation**: The element 23 is present at index 5.

> **Input**: arr[] = [1, 3, 5, 7, 9], x = 4  
> **Output**: -1  
> **Explanation**: The element 4 is not present in the array.

#### Description  
**Binary Search** is a searching algorithm that operates on a sorted or monotonic search space, repeatedly dividing it into halves to find a target value or optimal answer in logarithmic time **O(log N)**.

To apply Binary Search:
- The array must be **sorted**.
- Random access to elements should be possible (i.e., arrays or indexable lists).

#### Binary Search Algorithm  
- Divide the search space into two halves by finding the middle index `mid`.  
- Compare the middle element of the search space with the target.  
- If the target is found at the middle element, terminate the process.  
- If the target is smaller than the middle element, search the left half.  
- If the target is larger than the middle element, search the right half.  
- Repeat until the target is found or the search space is exhausted.

#### Solution  
For example: Consider an array **arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91}**, and the **target = 23**.

1. **Initial range**: low = 0, high = 9 → mid = 4 → arr[4] = 16 → 23 > 16 → search right half  
2. **New range**: low = 5, high = 9 → mid = 7 → arr[7] = 56 → 23 < 56 → search left half  
3. **New range**: low = 5, high = 6 → mid = 5 → arr[5] = 23 → Match found → return index 5

### Fibonacci Search  
*Coming soon…*

### Interpolation Search  
*Coming soon…*

### Jump Search  
*Coming soon…*

### Linear Search  
**Source**: [Linear Search Algorithm](https://www.geeksforgeeks.org/dsa/linear-search/)

#### Problem  
Given an array `arr[]` of `n` integers, and an integer element `x`, find whether element `x` is **present** in the array. Return the **index** of the first occurrence of `x` in the array, or **-1** if it doesn't exist.

> **Input**: arr[] = [1, 2, 3, 4], x = 3  
> **Output**: 2  
> **Explanation**: The element 3 is present at index 2.

> **Input**: arr[] = [10, 8, 30, 4, 5], x = 5  
> **Output**: 4  
> **Explanation**: The element 5 is present at index 4.

> **Input**: arr[] = [10, 8, 30], x = 6  
> **Output**: -1  
> **Explanation**: The element 6 is not present, so we return -1.

#### Description  
In Linear Search, we iterate over all the elements of the array and check if the current element is equal to the target. If we find any element equal to the target, we return its index. Otherwise, if no element matches, we return -1. Linear search is also known as **sequential search**.

#### Solution  
For example: Consider the array **arr[] = {10, 50, 30, 70, 80, 20, 90, 40}** and **target = 30**.

1. Compare the target with each element one by one starting from the first.  
2. Compare with the second element → not equal → move to next.  
3. Compare with the third element → match found → return index 2.

```python
def search(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":  # pragma: no cover
    arr = [2, 3, 4, 10, 40]
    x = 10
    result = search(arr, x)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
```
