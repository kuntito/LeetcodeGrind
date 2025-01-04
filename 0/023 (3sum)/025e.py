# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        # sort the array
        # looping through each element in `nums`
        # for each number, `n`
        # determine it's complement such that `n + comp = 0`
        # find all values at `i` and `j` where `i` and `j` are distinct indices after `n`'s index
        # such that `nums[i] + nums[j] == comp`
        # return an array containing those values
        # combine each element with `n` and update the final output `res`

        idx = 0
        dim = len(nums)
        while idx < dim:
            n = nums[idx]
            complement = -n

            for ts in self.twoSums(complement, idx + 1, nums):
                res.append(
                    [n] + ts
                )

            # to avoid duplicate `n`'s
            # if the number after `n` is the same as `n`
            # move forward
            while idx + 1 < dim and nums[idx + 1] == n:
                idx += 1

            idx += 1
        return res
    
    def twoSums(self, target, idx, nums):
        left = idx
        right = len(nums) - 1


        # 2, 2, 2, 3, 3, 5
        arr = []
        while left < right:
            a, b = nums[left], nums[right]
            total = a + b
            if total > target:
                right -= 1
                continue

            if total == target:
                arr.append(
                    [a, b],
                )

            while left + 1 < right and nums[left + 1] == a:
                left += 1
            left += 1

        return arr
