# https://leetcode.com/problems/ipo/description/

import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        pass
        # the target project while k >= 0
        # is the cheapest project i can afford
        # with the highest profit margins
        
        # you need a way to store the (profitMargin, fee)
        # use a maxHeap
        
        maxHeap = []
        for p, fee in zip(profits, capital):
            pass
            item = (-p, fee)
            heapq.heappush(maxHeap, item)
            
        funds = w
        
        found_project = True
        while k > 0 and found_project:
            to_add = []
            found_project = False
            while maxHeap:
                item = heapq.heappop(maxHeap)
                profit, fee = -1 * item[0], item[1]
                
                if funds >= fee:
                    funds += profit
                    found_project = True
                    k -= 1
                    break
                
                to_add.append(item)
                
            while to_add:
                heapq.heappush(maxHeap, to_add.pop())
                
                
        return funds
    
arr = [
    [2, 0, [1, 2, 3], [0, 1, 1]],
    [3, 0, [1, 2, 3], [0, 1, 2]],
]
a, b, c, d = arr[-1]
sol = Solution()
res = sol.findMaximizedCapital(a, b, c, d)
print(res)