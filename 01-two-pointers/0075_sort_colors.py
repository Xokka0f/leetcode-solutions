"""
LeetCode #75 — Sort Colors
https://leetcode.com/problems/sort-colors/

Сложность: Medium
Паттерн: Two Pointers (three pointers / Dutch National Flag)

Time: O(n)
Space: O(1)
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
            else:
                mid += 1
