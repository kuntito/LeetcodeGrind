class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        res = []

        for idx, n in enumerate(nums):
            if idx > 0 and n == nums[idx-1]: continue

            two_sums = self.twoSum(nums[idx+1:], -n)
            for ts in two_sums:
                res.append([n] + ts)

        return res


    def twoSum(self, nums, target):
        idx_left, idx_right = 0, len(nums) - 1
        res = []

        while idx_left < idx_right:
            left, right = nums[idx_left], nums[idx_right]
            total = left + right
            if total == target:
                res.append([left, right])
                while idx_left < len(nums) and nums[idx_left] == left:
                    idx_left += 1
            elif total > target:
                idx_right -= 1
            else:
                idx_left += 1
        
        return res


nums = [-1,0,1,2,-1,-4]
# nums = [-1, 0, 1, 0, 0, 0, 0]
nums = [0, 0, 0, 0, 0]
sol = Solution()

res = sol.threeSum(nums)
print(res)