# https://leetcode.com/problems/first-missing-positive/description/

# TODO https://neetcode.io/solutions/first-missing-positive
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        pass
        # set `smallest = 1`
        
        # iterate through `nums`
        # every time you find a n == smallest
        # inrease smallest by 1
        
        smallest = 1
        nums.sort()
        
        for n in nums:
            if n == smallest:
                smallest += 1
        
        
        return smallest
    
arr = [
    [1,2,0],
    [3,4,-1,1],
    [7,8,9,11,12],
    [100000, 3, 4000, 2, 15, 1, 99999],
]
foo = arr[-1]
sol = Solution()
res = sol.firstMissingPositive(foo)
print(res)

