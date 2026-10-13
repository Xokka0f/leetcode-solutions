"""
LeetCode #125 — Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Сложность: Easy
Паттерн: Two Pointers (opposite direction)

Time: O(n)
Space: O(n)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True
