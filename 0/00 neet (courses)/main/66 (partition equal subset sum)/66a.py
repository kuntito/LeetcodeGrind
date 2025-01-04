# https://leetcode.com/problems/partition-equal-subset-sum/


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        nums.sort()
        self.total = sum(nums)
        return self.explore(nums, 0, 0, {}) > 0
    
    def explore(self, nums, idx, part_sum, memo):
        if (idx, part_sum) in memo:
            return memo[(idx, part_sum)]

        double = part_sum * 2
        if idx == len(nums) or (double > self.total):
            return 0
        if double == self.total:
            return part_sum

        
        n = nums[idx]
        part_sum += n
        res = self.explore(nums, idx+1, part_sum, memo)
        memo[(idx+1, part_sum)] = res
        if res:
            return res
        part_sum -= n

        while idx + 1 < len(nums) and nums[idx + 1] == n:
            idx += 1
        res = self.explore(nums, idx+1, part_sum, memo)
        memo[(idx + 1, part_sum)] = res
        return memo[(idx+1, part_sum)]
    
arr = [
    [1, 2, 2],
    [1, 5, 11, 5],
    [1, 2, 3, 5]
]
foo = arr[-1]

sol = Solution()
res = sol.canPartition(foo)
print(res)