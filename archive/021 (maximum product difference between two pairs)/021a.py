# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/

class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums.sort()

        largest = nums[-1] * nums[-2]
        smallest = nums[0] * nums[1]
        return largest - smallest
    
arr = [
    [4,2,5,9,7,4,8],
    [5,6,2,7,4],
]
foo = arr[-1]
sol = Solution()
res = sol.maxProductDifference(foo)

print(res)