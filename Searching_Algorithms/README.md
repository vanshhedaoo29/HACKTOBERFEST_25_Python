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
#### Problem
Given an array, **arr[]** of **n** integers, and an integer element **x**, find whether element **x** is **present** in the array. Return the **index** of the first occurrence of **x** in the array, or **-1** if it doesn't exist.

> **Input**: arr[] = [1, 2, 3, 4], x = 3 <br>
> **Output**: 2 <br>
> **Explanation**: There is one test case with array as [1, 2, 3 4] and element to be searched as 3.Since 3 is present at index 2, the output is 2.
>
> **Input**: arr[] = [10, 8, 30, 4, 5], x = 5 <br>
> **Output**: 4 <br>
> **Explanation**: For array [10, 8, 30, 4, 5], the element to be searched is 5 and it is at index 4. So, the output is 4.
>
> **Input**: arr[] = [10, 8, 30], x = 6 <br>
> **Output**: -1 <br>
> **Explanation**: The element to be searched is 6 and its not present, so we return -1.

#### Description
In Linear Search, we iterate over all the elements of the array and check if it the current element is equal to the target element. If we find any element to be equal to the target element, then return the index of the current element. Otherwise, if no element is equal to the target element, then return -1 as the element is not found. Linear search is also known as **sequential search**.

#### Solution
For example: Consider the array **arr[] = {10, 50, 30, 70, 80, 20, 90, 40}** and **key = 30**
1. Compare the key with each element one by one starting from the 1st element.
2. Compare the key with the 2nd element which is not equal to the key, so move to the next element.
3. Compare the key with the 3rd element. Key is found so stop the search.

```python
def search(arr, x):
    n = len(arr)
    
    # Iterate over the array in order to
    # find the key x
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10

    result = search(arr, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
```

### Fibonacci Search
*Coming soon…*

### Interpolation Search
*Coming soon…*

### Jump Search
*Coming soon…*

### Linear Search
*Coming soon…*
