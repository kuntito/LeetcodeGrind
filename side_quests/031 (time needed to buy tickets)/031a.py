# https://leetcode.com/problems/time-needed-to-buy-tickets/description/

class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        # while tickets[k] is greater than zero
        # loop through tickets, keeping track of how many times
        # a number > 0 was decremented

        count = 0
        while True:
            for idx, tic in enumerate(tickets):
                if tic:
                    tickets[idx] -= 1
                    count += 1
                if tickets[k] == 0:
                    return count

arr = [
    [[5,1,1,1], 0],
    [[2,3,2], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.timeRequiredToBuy(foo, bar)
print(res)
