"""
LeetCode #11 — Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Сложность: Medium
Паттерн: Two Pointers (opposite direction)

Time: O(n)
Space: O(1)
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maximum = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > maximum:
                maximum = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum
