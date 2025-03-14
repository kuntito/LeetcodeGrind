# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pass
        pos_idx, neg_idx = 0, 0
        dim = len(nums)
        
        res = []
        while pos_idx < dim and neg_idx < dim:
            pass
            # move to the first positive number
            while pos_idx < dim and nums[pos_idx] < 0:
                pos_idx += 1
                
            # move to the first negative number
            while neg_idx < dim and nums[neg_idx] >= 0:
                neg_idx += 1
                
            if pos_idx < dim:
                res.append(nums[pos_idx])
            
            if neg_idx < dim:
                res.append(nums[neg_idx])
                
            pos_idx += 1
            neg_idx += 1
                
        while pos_idx < dim:
            while pos_idx < dim and nums[pos_idx] < 0:
                pos_idx += 1
            if pos_idx < dim:
                res.append(nums[pos_idx])
            
            pos_idx += 1

        while neg_idx < dim:
            while neg_idx < dim and nums[neg_idx] >= 0:
                neg_idx += 1
            
            if neg_idx < dim:
                res.append(nums[neg_idx])
                
            neg_idx += 1
                
        return res
    
arr = [
    [3,1,-2,-5,2,-4],
    [-1,1],
]
foo = arr[-1]
sol = Solution()
res = sol.rearrangeArray(foo)

print(res)