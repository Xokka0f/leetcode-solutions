"""
LeetCode #16 — 3Sum Closest
https://leetcode.com/problems/3sum-closest/

Сложность: Medium
Паттерн: Two Pointers (opposite direction) + Sort

Time: O(n²)
Space: O(1)
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        sorted_nums = sorted(nums)
        min_distance = float("inf")
        for i in range(len(sorted_nums)):
            left = i + 1
            right = len(sorted_nums) - 1
            while left < right:
                cur_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if abs(cur_sum - target) == 0:
                    return cur_sum
                elif abs(cur_sum - target) < abs(min_distance - target):
                    min_distance = cur_sum
                if cur_sum < target:
                    left += 1
                else:
                    right -= 1
        return min_distance
