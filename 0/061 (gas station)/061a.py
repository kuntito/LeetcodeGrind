# https://leetcode.com/problems/gas-station/description/


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        dim = len(gas)
        # combined = [gas[idx] - cost[idx] for idx in range(dim)]
        if len(gas) == 1 and gas[0] - cost[0] >= 0:
            return 0

        left, right = 0, 0
        streakPos = None

        streak = 0
        total = 0
        while right < len(gas):
            n = gas[right] - cost[right]
            total += n
            streak += n

            if streak > 0:
                if streakPos is None:
                    streakPos = [left, right]
                else:
                    streakPos[0] = left
                    streakPos[1] = right
            else:
                streak = 0
                left = right + 1
            right += 1


        # total = sum(combined)
        return streakPos[0] if total >= 0 else -1
    

arr = [
    [
        [2, 3, 4],
        [3, 4, 3]
    ],
    [[2], [2]],
    # [[1,2,3,4,5], [3,4,5,1,2]],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.canCompleteCircuit(foo, bar)
print(res)