"""
LeetCode #167 — Two Sum II
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Сложность: Easy
Паттерн: Two Pointers (opposite direction)

Time: O(n)
Space: O(1)
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
