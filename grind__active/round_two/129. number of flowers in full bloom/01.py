from collections import defaultdict
import heapq
from typing import List

class Solution:
    def fullBloomFlowers(
        self,
        flowers: List[List[int]],
        people: List[int]
    ) -> List[int]:
        flowerMap = defaultdict(int)
        
        for start, end in flowers:
            for i in range(start, end+1):
                flowerMap[i] += 1
            
        res = []    
        for p in people:
            res.append(flowerMap[p])
            
        return res
    
arr = [
    [
        [[1,6],[3,7],[9,12],[4,13]],
        [2,3,7,11],
    ]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.fullBloomFlowers(foo, bar)
print(res)