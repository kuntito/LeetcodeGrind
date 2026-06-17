import heapq
from typing import List

class Solution:
    def findMaximizedCapital(
        self,
        k: int,
        w: int,
        profits: List[int],
        capital: List[int]
    ) -> int:
        self.canAfford = []
        self.outOfReach = []
        
        # put every project in out of reach
        # then pop the ones you can afford
        
        # how am i storing the projects?
        # for out of reach, a tuple.
        # (capital, profits)
        
        # for can afford, a different tuple
        # (profits, capital)
        
        self.populateOutOfReach(profits, capital)
        
        self.capital = w
        self.projectCount = 0
        self.populateCanAfford()
        
        while self.projectCount < k and self.canAfford:
            p, c = heapq.heappop(self.canAfford)
            p = -1 * p
            
            # self.capital -= c
            self.capital += p
            self.projectCount += 1
            
            self.populateCanAfford()
        
        return self.capital
    
        
    def populateOutOfReach(self, profits, capital):
        for p, c in zip(profits, capital):
            heapq.heappush(
                self.outOfReach,
                (
                    c, 
                    p
                )
            )
            
    def populateCanAfford(self):
        while self.outOfReach and self.capital >= self.outOfReach[0][0]:
            c, p = heapq.heappop(self.outOfReach)
            
            heapq.heappush(
                self.canAfford,
                (
                    -1 * p, 
                    c
                )
            )
            
arr = [
    [
        2,
        0,
        [1, 2, 3],
        [0, 1, 1],
    ]
]
uno, dos, tres, qua = arr[-1]
sol = Solution()
res = sol.findMaximizedCapital(uno, dos, tres, qua)
print(res)