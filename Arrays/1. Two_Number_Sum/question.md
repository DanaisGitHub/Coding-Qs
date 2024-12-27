## Two Number Sum Array

You are given an array of integers and a target sum. Your task is to write a function that finds all pairs of numbers in the array that add up to the target sum. You may assume that the array contains unique elements and the target sum can always be achieved by using two numbers from the array.

Write a function called `findNumberPairs(array, targetSum)` that takes in two parameters:

- `array` (an array of integers): The array of unique integers.
- `targetSum` (an integer): The target sum.

The function should return an array of arrays, where each inner array represents a pair of numbers that add up to the target sum. Each pair should be sorted in ascending order.

### Example

**Input:**
```python
array = [2, 4, 5, 7, 9]
targetSum = 11
```

Output
**Output:**
```python
[[2, 9], [4, 7]]
```

[[2, 9], [4, 7]]

Note:
You may not use the same element twice to form a pair.
The order of the pairs in the output array does not matter.
