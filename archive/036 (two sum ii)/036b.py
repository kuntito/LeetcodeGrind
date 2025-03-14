# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        uno, dos = 0, len(numbers) - 1

        while uno < dos:
            agg = numbers[uno] + numbers[dos]
            if agg == target:
                return [uno + 1, dos + 1]
            elif agg > target:
                dos -= 1
            else:
                uno += 1
