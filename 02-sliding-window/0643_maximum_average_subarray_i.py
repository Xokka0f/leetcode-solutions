"""
LeetCode #643 — Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/

Сложность: Easy
Паттерн: Sliding Window (fixed size)

Time: O(n)
Space: O(1)
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_avg = window_sum
        for right in range(k, len(nums)):
            window_sum += nums[right]
            window_sum -= nums[right - k]
            max_avg = max(max_avg, window_sum)
        return max_avg / k
