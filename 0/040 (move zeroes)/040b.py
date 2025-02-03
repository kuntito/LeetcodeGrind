# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        s = 0
        for idx in range(len(nums)):
            val = nums[idx]
            if val:
                nums[idx], nums[s] = nums[s], nums[idx]
                s += 1



arr = [
    [0,1,0,3,12],
    [0],
]
foo = arr[-1]
sol = Solution()
sol.moveZeroes(foo)
print(foo)