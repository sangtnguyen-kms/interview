## Problem Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Example
```python
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

## Test case
Sure, here are 10 test cases for the "Two Sum" problem:
```py
1. nums = [2, 7, 11, 15], target = 9 -> Expected output: [0, 1]
2. nums = [3, 2, 4], target = 6 -> Expected output: [1, 2]
3. nums = [3, 3], target = 6 -> Expected output: [0, 1]
4. nums = [1, 2, 3, 4, 5], target = 9 -> Expected output: [3, 4]
5. nums = [1, 2, 3, 4, 5], target = 7 -> Expected output: [1, 3]
6. nums = [1, 2, 3, 4, 5], target = 10 -> Expected output: [4, 0]
7. nums = [1, 2, 3, 4, 5], target = 11 -> Expected output: [4, 2]
8. nums = [1, 2, 3, 4, 5], target = 6 -> Expected output: [1, 2]
9. nums = [1, 2, 3, 4, 5], target = 1 -> Expected output: None
10. nums = [], target = 5 -> Expected output: None
```