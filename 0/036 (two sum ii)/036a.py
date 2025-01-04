# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}
        for idx, n in enumerate(numbers):
            compliment = target - n
            if compliment in seen:
                return [
                    seen[compliment],
                    idx
                ]
            seen[n] = idx