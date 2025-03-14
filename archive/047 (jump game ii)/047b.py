# https://leetcode.com/problems/jump-game-ii/description/


class Solution:
    def jump(self, nums: list[int]) -> int:
        if nums[0] == 0: return 0

        count = -1
        seen = set()
        seen.add(0)
        while seen:
            count += 1
            temp = set()

            for idx in seen:
                jump = nums[idx]
                for i in range(jump):
                    next_idx = idx + i + 1
                    if next_idx in seen or next_idx >= len(nums):
                        continue

                    temp.add(next_idx)
            seen = temp

        return count





arr = [
    [3, 0, 1, 4],
    [2, 3, 0, 1, 4],
    [3, 2, 1],
    [3],
]
foo = arr[-1]
sol = Solution()
res = sol.jump(foo)
print(res)