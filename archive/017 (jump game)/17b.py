# https://leetcode.com/problems/jump-game/description/

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goalpost = len(nums) - 1

        for idx in range(goalpost, -1, -1):
            jump = nums[idx]
            if idx + jump >= goalpost:
                goalpost = idx

        return goalpost == 0