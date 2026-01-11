# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        pass
        # sort `nums`
        nums.sort()
        # declare an array, `arr`, that represents the prefix sum of `nums`
       
        prefixSum = self.get_prefix_sum(nums)
         
        
        # iterating backwards through `nums`
        # if the prefix sum at `arr[idx-1]` is greater than the `nums[idx]`
        # return prefixSum + nums[idx]
        dim = len(nums)
        for idx in range(dim - 1, -1, -1):
            n = nums[idx]
            prefix = prefixSum[idx - 1] if idx - 1 >= 0 else None
            if prefix and prefix > n:
                return prefix + n
            
        return -1
        
        
    def get_prefix_sum(self, arr):
        pref = []
    
        tmp = 0
        for n in arr:
            tmp += n
            pref.append(tmp)
            
        return pref
    
arr = [
    [1,12,1,2,5,50,3],
    [5, 5, 5],
    [5,5,50],
]
foo = arr[-1]
sol = Solution()
res = sol.largestPerimeter(foo)

print(res)