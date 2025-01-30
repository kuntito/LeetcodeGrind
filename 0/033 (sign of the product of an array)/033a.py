# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        # loop through the array keep track of all negative numbers
        negCount = 0
        for n in nums:
            if n < 0:
                negCount += 1
            # if you hit `0`, return `0`
            if n == 0:
                return 0


        # after looping return 1 if there are an even number of negatives
        # else return -1
        return -1 if negCount % 2 else 1
    
arr = [
    [-1,1,-1,1,-1],
    [-1,-2,-3,-4,3,2,1],
    [1,5,0,2,-3],
]
foo = arr[-1]
sol = Solution()
res = sol.arraySign(foo)
print(res)
