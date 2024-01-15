## Problem Description

Given a string s, find the length of the longest substring without repeating characters.

## Example
```py
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
python
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
python
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```
## Constraints

- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

## Test case
```py
1. s = "abcabcbb" -> Expected output: 3
2. s = "bbbbb" -> Expected output: 1
3. s = "pwwkew" -> Expected output: 3
4. s = "aab" -> Expected output: 2
5. s = "dvdf" -> Expected output: 3
6. s = " "  -> Expected output: 1
7. s = "abba" -> Expected output: 2
8. s = "a" -> Expected output: 1
9. s = "" -> Expected output: 0
10. s = "abcdefghijklmnopqrstuvwxyz" -> Expected output: 26
```