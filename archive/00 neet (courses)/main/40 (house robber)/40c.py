class Solution:
    def rob(self, nums: list[int]) -> int:
        second_last, last = 0, 0

        for n in nums:
            temp = last
            last = max(n + second_last, last)
            second_last = last

        return last
            


nums = [2, 1, 3, 8]
# nums = [2, 7, 9, 3, 1]

sol = Solution()
res = sol.rob(nums)

print(res)