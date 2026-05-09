from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[-1] * (k + 1) for _ in range(n)]

        def dfs(i, m):
            if i == n:
                return 0 if m == 0 else float("inf")
            if m == 0:
                return float("inf")
            if dp[i][m] != -1:
                return dp[i][m]

            res = float("inf")
            curSum = 0
            for j in range(i, n - m + 1):
                curSum += nums[j]
                res = min(res, max(curSum, dfs(j + 1, m - 1)))

            dp[i][m] = res
            return res

        return dfs(0, k)