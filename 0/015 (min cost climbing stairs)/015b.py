# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        penul, ul = 0, 0
        for idx in range(len(cost) - 1, -1, -1):
            cost[idx] += min(penul,ul)
            ul, penul = penul, cost[idx]


        return min(cost[0],cost[1])





arr = [
    [0,2,2,1],
    [10, 15, 20],
    [1,100,1,1,1,100,1,1,100,1],
]

foo = arr[-1]
sol = Solution()
res = sol.minCostClimbingStairs(foo)
print(res)