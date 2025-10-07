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
  - [Fibonacci Search](#fibonacci-search)
    - [Problem](#problem-1)
    - [Code](/Searching_Algorithms/fibonacci_search.py)
  - [Interpolation Search](#interpolation-search)
    - [Problem](#problem-2)
    - [Code](/Searching_Algorithms/interpolation_search.py)
  - [Jump Search](#jump-search)
    - [Problem](#problem-3)
    - [Code](/Searching_Algorithms/jump_search.py)
  - [Linear Search](#linear-search)
    - [Problem](#problem-4)
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
**Source**: [Fibonacci Search](https://www.geeksforgeeks.org/dsa/fibonacci-search/)

#### Problem  
Given a **sorted array** `arr[]` of size `n` and an integer `x`, check whether `x` is present in the array. Return the **index** of `x` if found, or **-1** if it is not present.

> **Input**: arr[] = [2, 3, 4, 10, 40], x = 10  
> **Output**: 3  
> **Explanation**: 10 is present at index 3.

> **Input**: arr[] = [2, 3, 4, 10, 40], x = 11  
> **Output**: -1  
> **Explanation**: 11 is not present in the given array.

#### Description  
Fibonacci Search is a comparison-based technique that uses Fibonacci numbers to search for an element in a **sorted array**. It is similar to Binary Search in that it uses a divide-and-conquer strategy and has logarithmic time complexity.

#### Similarities with Binary Search  
- Works only on **sorted arrays**  
- Divide and conquer algorithm  
- Time complexity: **O(log n)**

#### Differences from Binary Search  
- Fibonacci Search divides the array into **unequal parts**  
- It avoids the division operator (`/`) and instead uses **addition and subtraction**  
- This can be beneficial on CPUs where division is costly  
- It examines **closer elements** in subsequent steps, which may help when the array is too large to fit in CPU cache or RAM

#### Background  
Fibonacci numbers are defined recursively as:  
- F(0) = 0, F(1) = 1  
- F(n) = F(n-1) + F(n-2)

First few Fibonacci numbers:  
`0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...`

Approximate relationships used in the algorithm:  
- F(n - 2) ≈ (1/3) * F(n)  
- F(n - 1) ≈ (2/3) * F(n)

#### Fibonacci Search Algorithm  
1. Find the smallest Fibonacci number greater than or equal to the length of the array (`n`). Let this be `fibM`.  
2. Let `fibMm1` and `fibMm2` be the two preceding Fibonacci numbers.  
3. Initialize `offset = -1`.  
4. While `fibM > 1`:
   - Compare `arr[min(offset + fibMm2, n-1)]` with `x`.
   - If equal, return the index.
   - If `x < arr[i]`, move the Fibonacci window two steps down.
   - If `x > arr[i]`, move the window one step down and update `offset = i`.
5. If one element remains (`fibMm1 == 1`), check if it matches `x`.

#### Solution  
Let’s walk through an example:

```text
arr[] = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
x = 85
```

- Length of array `n = 11`
- Smallest Fibonacci number ≥ 11 is `13`
- Initial Fibonacci numbers: `fibM = 13`, `fibMm1 = 8`, `fibMm2 = 5`
- Start with `offset = -1`
- Compare `arr[4] = 45` → 85 > 45 → move window forward
- Update `offset = 4`, Fibonacci numbers shift
- Compare `arr[7] = 82` → 85 > 82 → move window forward
- Update `offset = 7`, Fibonacci numbers shift
- Compare `arr[8] = 85` → match found → return index 8


### Interpolation Search  
**Source**: [Interpolation Search](https://www.geeksforgeeks.org/dsa/interpolation-search/)

#### Problem  
Given a **sorted array** `arr[]` of `n` uniformly distributed values and a target element `x`, search for `x` and return its index if found, otherwise return -1.

> **Input**: arr[] = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23], x = 18  
> **Output**: 4  
> **Explanation**: The element 18 is present atgit s index 4.

> **Input**: arr[] = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23], x = 17  
> **Output**: -1  
> **Explanation**: The element 17 is not present in the array.

#### Description
Interpolation Search improves on Binary Search when values are uniformly distributed. Instead of always probing the middle element, it probes a position computed by estimating where the target should be relative to the values at the current low and high indices, so searches tend to move closer to the target on average.

#### Probe Position Formula
The probe position `pos` is computed as:
```text
pos = lo + ((x - arr[lo]) * (hi - lo)) / (arr[hi] - arr[lo])
```
This formula returns a higher `pos` when `x` is closer to `arr[hi]` and a smaller `pos` when `x` is closer to `arr[lo]`.

#### Algorithm
1. Initialize `lo` and `hi` to the bounds of the array.
2. While `lo <= hi` and `x` is between `arr[lo]` and `arr[hi]`:
    - Compute `pos` using the probe position formula.
    - If `arr[pos] == x`, return `pos`.
    - If `arr[pos] < x`, set `lo = pos + 1`.
    - If `arr[pos] > x`, set `hi = pos - 1`.
3. If a match is not found, return -1.

### Jump Search
**Source**: [Jump Search](https://www.geeksforgeeks.org/dsa/jump-search/)

#### Problem  
Given a **sorted array** `arr[]` of `n` elements and a target value `x`, find the **index** of `x` if it is present in the array. Otherwise, return **-1**.

> **Input**: arr[] = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], x = 55  
> **Output**: 10  
> **Explanation**: The element 55 is present at index 10.

#### Description  
**Jump Search** is a searching algorithm for **sorted arrays** that reduces the number of comparisons by jumping ahead by fixed steps instead of checking every element. Once the interval containing the target is found, a **linear search** is performed within that block.

It is more efficient than **Linear Search**, but generally slower than **Binary Search**.

#### Key Characteristics  
- Works only on **sorted arrays**  
- Optimal jump size is **√n**  
- Time complexity: **O(√n)**  
- Auxiliary space: **O(1)**  
- Useful when division operations are costly or when binary search is not ideal

#### Jump Search Algorithm  
1. Calculate the optimal block size `m = √n`.  
2. Start at index `0`, and jump ahead by `m` until `arr[j] ≥ x` or end of array is reached.  
3. Once the block is found, perform a **linear search** from the previous jump point to the current index.  
4. If the target is found, return its index. Otherwise, return -1.

#### Solution  
Let’s walk through an example:

```text
arr[] = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = 55
```

- Array length `n = 16` → optimal jump size `m = √16 = 4`
- Jump from index 0 → 4 → 8 → 12  
- At index 12, `arr[12] = 144` > 55 → jump back to index 8  
- Perform linear search from index 8 to 12  
- `arr[10] = 55` → match found → return index 10


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
