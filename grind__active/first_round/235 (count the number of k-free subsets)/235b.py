# https://leetcode.com/problems/count-the-number-of-k-free-subsets/description/

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: list[int], k: int) -> int:
        pass
    
        # recursively create every possible subset
        # at each iteration, you can either pick one element
        # or none
        # however, the element you pick must not have a k-complement existing in the set
        
        self.res = 0
        self.explore(0, nums, k, set())
        
        return self.res
    
    def explore(self, idx, nums, k, currSet):
        if idx == len(nums):
            self.res += 1
            return
        
        self.explore(idx + 1, nums, k, currSet)
        
        n = nums[idx]
        
        # only add if `n` meets the `k` constraint
        if self.isMeetConstraint(n, k, currSet):
            currSet.add(n)
            self.explore(idx + 1, nums, k, currSet)
            currSet.remove(n)
            
            
    def isMeetConstraint(self, num, k, currSet):
        leftComplement = num - k
        rightComplement = num + k
        return leftComplement not in currSet and rightComplement not in currSet
        

arr = [
    [[5,4,6], 1],
    [[2,3,5,8], 5],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.countTheNumOfKFreeSubsets(foo, bar)
print(res)