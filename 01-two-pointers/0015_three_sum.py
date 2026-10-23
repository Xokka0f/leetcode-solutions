"""
LeetCode #15 — 3Sum
https://leetcode.com/problems/3sum/

Сложность: Medium
Паттерн: Two Pointers (opposite direction) + Sort

Time: O(n²)
Space: O(1)
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_list = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            left = i + 1
            right = len(sorted_nums) - 1
            while left < right:
                total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                if total == 0:
                    result_list.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result_list
