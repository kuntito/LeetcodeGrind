# https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        # grab the super set of numbers
        num_set = {n for n in range(1, len(nums) + 1)}

        duplicate = None
        while nums:
            n = nums.pop()
            # if `n` is in the set, remove it
            # this is the first occurrence of `n`
            if n in num_set:
                num_set.remove(n)
            else:
                # if you find `n` again, it must be a duplicate
                duplicate = n
        
        return [duplicate] + list(num_set)
    
arr = [
    [1,2,2,4],
]
foo = arr[-1]
sol = Solution()
res = sol.findErrorNums(foo)
print(res)