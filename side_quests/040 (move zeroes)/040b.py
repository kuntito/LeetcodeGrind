# https://leetcode.com/problems/move-zeroes/description/

# TODO why does this work?
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums



arr = [
    [0,1,0,3,12],
    [0],
]
foo = arr[-1]
sol = Solution()
sol.moveZeroes(foo)
print(foo)