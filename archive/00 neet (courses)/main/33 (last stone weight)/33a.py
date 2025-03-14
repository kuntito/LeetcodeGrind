# https://leetcode.com/problems/last-stone-weight/description/

import heapq

class Solution:
    def lastStoneWeight(self, stones: list) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)


        while len(stones) > 1:
            alpha, sigma = -heapq.heappop(stones), -heapq.heappop(stones)
            
            diff = abs(alpha - sigma)
            if diff:
                stones.append(-diff)

        return -stones[0] if stones else 0
    

bar = [8, 4, 1, 2]
sol = Solution()

res = sol.lastStoneWeight(bar)
print(res)