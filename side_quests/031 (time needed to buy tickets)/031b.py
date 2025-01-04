# https://leetcode.com/problems/time-needed-to-buy-tickets/description/


# TODO https://www.youtube.com/watch?v=cVmS9N6kf2Y
# 2:35
from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        queue = deque()
        for idx, tic in enumerate(tickets):
            queue.append((idx, tic))

        count = 0
        while queue:
            idx, tic = queue.popleft()

            # remove and decrement tic from the start of queue
            # if `tic > 0`, increment count
            # append (idx, tic) to queue

            # if tic == 0 and idx == k:
            # return count








arr = [
    [[5,1,1,1], 0],
    [[2,3,2], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.timeRequiredToBuy(foo, bar)
print(res)
