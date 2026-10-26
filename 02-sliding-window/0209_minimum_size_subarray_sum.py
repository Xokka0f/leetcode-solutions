"""
LeetCode #209 — Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Сложность: Medium
Паттерн: Sliding Window (dynamic size)

Time: O(n)
Space: O(1)
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        min_len = float("inf")
        win_sum = 0
        for right in range(len(nums)):
            win_sum += nums[right]
            while win_sum >= target:
                min_len = min(min_len, right - left + 1)
                win_sum -= nums[left]
                left += 1
        return min_len if min_len != float("inf") else 0
