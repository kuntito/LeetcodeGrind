# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/


class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        maxOne = 0
        maxTwo = 0

        minOne = float("inf")
        minTwo = float("inf")

        for n in nums:
            if n > maxOne:
                if maxOne > 0:
                    maxTwo = maxOne
                maxOne = n
            elif n > maxTwo:
                maxTwo = n

            if n < minOne:
                if minOne < float("inf"):
                    minTwo = minOne
                minOne = n
            elif n < minTwo:
                minTwo = n

        return (maxOne * maxTwo) - (minOne * minTwo)
    
arr = [
    [5,6,2,7,4],
    [4,2,5,9,7,4,8],
]
foo = arr[-1]
sol = Solution()
res = sol.maxProductDifference(foo)

print(res)