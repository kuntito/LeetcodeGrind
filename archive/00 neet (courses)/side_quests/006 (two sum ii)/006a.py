# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        left_idx, right_idx = 0, len(numbers) - 1

        while left_idx < right_idx:
            former, latter = numbers[left_idx], numbers[right_idx]
            foo = former + latter
            if foo == target:
                return [left_idx + 1, right_idx + 1]
            elif foo > target:
                right_idx -= 1
            else:
                left_idx += 1


numbers = [2,7,11,15]
target = 9
sol = Solution()
res = sol.twoSum(numbers, target)

print(res)