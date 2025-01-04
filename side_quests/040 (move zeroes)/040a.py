# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # iterate through `nums` from behind,
        # every zero found should swap with it's right element
        # if the element is NOT zero
        
        dim = len(nums)
        for idx in range(dim-1, -1, -1):
            val = nums[idx]
            if val == 0:
                self.move_to_end(idx, nums)

    def move_to_end(self, idx, nums):
        while idx + 1 < len(nums) and nums[idx + 1] != 0:
            nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
            idx += 1

arr = [
    [0,1,0,3,12],
    [0],
]
foo = arr[-1]
sol = Solution()
sol.moveZeroes(foo)
print(foo)