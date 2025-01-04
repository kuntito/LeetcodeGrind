# https://leetcode.com/problems/jump-game/description/

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        dp = [False for _ in nums]
        dp[-1] = True

        last_idx = len(nums) - 1
        for idx in range(last_idx, -1, -1):
            jump = nums[idx]

            farthest_idx = idx + jump
            if farthest_idx >= last_idx:
                dp[idx] = True
            else:
                cursor = farthest_idx
                while cursor > idx:
                    if dp[cursor]:
                        dp[idx] = True
                    cursor -= 1


        return dp[0]
            



arr = [
    [3,2,1,0,4],
    [2, 3, 1, 1, 4],
]
foo = arr[-1]
sol = Solution()
res = sol.canJump(foo)

print(res)