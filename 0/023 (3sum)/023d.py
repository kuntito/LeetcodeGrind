# https://leetcode.com/problems/3sum/description/


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for idx, n in enumerate(nums):
            if idx > 0 and n == nums[idx - 1]:
                continue

            start, end = idx + 1, len(nums) - 1
            while start < end:
                a, b = nums[start], nums[end]
                three_sum = n + a + b
                if three_sum == 0:
                    res.append([n, nums[start], nums[end]])
                    while start <= end and nums[start] == a:
                        start += 1
                elif three_sum > 0:
                    end -= 1
                else:
                    start += 1

        return res