class Solution:
    def subsets(self, nums: list) -> list:
        res = []
        subset = []
        self.dfs(0, res, subset, nums)
        return res
    
    
    def dfs(self, idx, res, subset, nums):
        if idx >= len(nums):
            res.append(subset.copy())
            return
        
        subset.append(nums[idx])
        self.dfs(idx + 1, res, subset, nums)

        subset.pop()
        self.dfs(idx + 1, res, subset, nums)