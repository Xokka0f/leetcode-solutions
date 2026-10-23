"""
LeetCode #977 — Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/

Сложность: Easy
Паттерн: Two Pointers (opposite direction)

Time: O(n)
Space: O(n)
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        len_n = len(nums)
        left = 0
        right = len_n - 1
        pos = len_n - 1
        new_list = [0] * len_n
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                new_list[pos] = nums[right] ** 2
                right -= 1
            else:
                new_list[pos] = nums[left] ** 2
                left += 1
            pos -= 1
        return new_list
