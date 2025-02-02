# https://leetcode.com/problems/time-needed-to-buy-tickets/description/

# TODO https://neetcode.io/solutions/time-needed-to-buy-tickets
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        pass

        res = 0

        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:
                # TODO deep this condition
                res += min(tickets[i], tickets[k] - 1)
        
        return res






arr = [
    [[5,1,1,1], 0],
    [[2,3,2], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.timeRequiredToBuy(foo, bar)
print(res)
