# https://leetcode.com/problems/jump-game-ii/description/


class Solution:
    def jump(self, nums: list[int]) -> int:
        self.nums = nums
        memo = {}
        for idx in range(len(nums) - 1, -1, -1):
            self.explore(idx, 0, memo)
        
        return memo[0][1]


    def explore(self, idx, jump_count, memo):
        if idx in memo:
            flag, count = memo[idx]
            return  flag, jump_count + count
        
        if idx >= len(self.nums) - 1:
            memo[idx] = (True, jump_count)
            return memo[idx]
        
        n = self.nums[idx]
        if n == 0:
            memo[idx] = (False, jump_count)
            return memo[idx]
        
        min_count = len(self.nums)
        for count in range(1, n + 1):
            is_reach, count = self.explore(
                idx + count,
                jump_count + 1,
                memo,
            )
            if is_reach:
                min_count = min(
                    min_count,
                    count
                )

        foo = (True, min_count) if min_count != len(self.nums) else (False, min_count)
        memo[idx] = foo
        return memo[idx]





arr = [
    [2, 3, 0, 1, 4],
    [3, 0, 1, 4],
    [3, 2, 1],
]
foo = arr[-1]
sol = Solution()
res = sol.jump(foo)
print(res)