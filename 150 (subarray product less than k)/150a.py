# https://leetcode.com/problems/subarray-product-less-than-k/description/

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        pass
        # create a prefix product
        # run through all possible sub arrays and count those that meet the criteria
        
        prefixProd = self.get_prefix_prod(nums)
        count = 0
        dim = len(nums)
        
        for unit in range(1, dim + 1):
            pass
            for j in range(dim-(unit - 1)):
                slice_start = j
                slice_end = slice_start + unit
                
                prodBefore = prefixProd[slice_start-1] if slice_start - 1 >= 0 else 1
                prod = prefixProd[slice_end - 1] / prodBefore
                # print(nums[slice_start:slice_end], prod)
                if prod < k:
                    count += 1
                    
        return count
        
    def get_prefix_prod(self, nums):
        pref = []
        
        tmp = 1
        for n in nums:
            tmp *= n
            
            pref.append(tmp)
            
            
        return pref
    
arr = [
    [[10,5,2,6], 100],
    [[1,2,3], 0],
    [[1,1,1], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.numSubarrayProductLessThanK(foo, bar)
print(res)