# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        idx = len(cost) - 1
        while idx >= 0:
            cost[idx] += min(
                cost[idx + 1] if idx + 1 < len(cost) else 0,
                cost[idx + 2] if idx + 2 < len(cost) else 0
            )
            idx -= 1


        return min(
            cost[0],
            cost[1]
        )





arr = [
    [0,2,2,1],
    [1,100,1,1,1,100,1,1,100,1],
    [10, 15, 20],
]

foo = arr[-1]
sol = Solution()
res = sol.minCostClimbingStairs(foo)
print(res)