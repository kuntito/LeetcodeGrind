# https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        num_set = {n for n in range(1, len(nums) + 1)}

        res = []
        while nums:
            n = nums.pop()
            if n in num_set:
                num_set.remove(n)
            else:
                res.append(n)
        
        return res + list(num_set)
    
arr = [
    [1,2,2,4],
]
foo = arr[-1]
sol = Solution()
res = sol.findErrorNums(foo)
print(res)