# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            num = numbers[start] + numbers[end]
            if num > target:
                end -= 1
            elif num < target:
                start += 1
            else:
                return [start+1, end+1]