# https://leetcode.com/problems/number-of-good-pairs/description/

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        res = 0
        count = {}
        for n in nums:
            if n in count:
                # the number of existing `n`'s determine how many pairs can be formed
                # since the new addition can form a pair with each `n`
                res += count[n]
                count[n] += 1
            else:
                count[n] = 1
        return res
    
    
arr = [
    [1,2,3,1,1,3],
    [1,2,3],
    [1, 1, 1],
    [1,1,1,1],
]
foo = arr[-1]
sol = Solution()
res = sol.numIdenticalPairs(foo)
print(res)

