# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/1440684401/

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        super_set = {i for i in range(1, len(nums) + 1)}

        for n in nums:
            if n in super_set:
                super_set.remove(n)
        

        return list(super_set)
    
arr = [
    [1, 1],
    [4,3,2,7,8,2,3,1],
    [1],
]
foo = arr[-1]
sol = Solution()
res = sol.findDisappearedNumbers(foo)
print(res)
