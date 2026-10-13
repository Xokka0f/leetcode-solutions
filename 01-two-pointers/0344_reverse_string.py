"""
LeetCode #344 — Reverse String
https://leetcode.com/problems/reverse-string/

Сложность: Easy
Паттерн: Two Pointers (opposite direction)

Time: O(n)
Space: O(1)
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
