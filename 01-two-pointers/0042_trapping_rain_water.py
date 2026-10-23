"""
LeetCode #42 — Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Сложность: Hard
Паттерн: Two Pointers (opposite direction)

Time: O(n)
Space: O(1)
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < max_left:
                    water += max_left - height[left]
                else:
                    max_left = height[left]
                left += 1
            else:
                if height[right] < max_right:
                    water += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1
        return water
