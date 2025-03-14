# https://leetcode.com/problems/concatenation-of-array/description/

class Solution:
    def getConcatenation(self, nums):
        ans = []
        for n in nums:
            ans.append(n)
        for n in nums:
            ans.append(n)

        return ans
    

nums = [1, 2, 1]
foo = Solution()
res = foo.getConcatenation(nums)

print(res)