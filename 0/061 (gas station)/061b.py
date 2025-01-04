# https://leetcode.com/problems/gas-station/description/

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(cost) > sum(gas): return -1
        dim = len(cost)

        total = 0
        res = 0
        for idx in range(dim):
            total += gas[idx] - cost[idx]

            if total < 0:
                res = idx + 1
                total = 0
            
        return res
    

arr = [
    [[2], [2]],
    # [[1,2,3,4,5], [3,4,5,1,2]],
    [
        [2, 3, 4],
        [3, 4, 3]
    ],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.canCompleteCircuit(foo, bar)
print(res)