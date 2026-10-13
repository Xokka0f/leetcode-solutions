"""
LeetCode #283 — Move Zeroes
https://leetcode.com/problems/move-zeroes/

Сложность: Easy
Паттерн: Two Pointers (same direction)

Time: O(n)
Space: O(1)
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
