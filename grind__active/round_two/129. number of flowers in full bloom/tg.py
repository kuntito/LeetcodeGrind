from collections import defaultdict
import heapq
from typing import List

class Solution:
    def fullBloomFlowers(
        self,
        flowers: List[List[int]],
        people: List[int]
    ) -> List[int]:
        startHeap = []
        endHeap = []

        for s, e in flowers:
            startHeap.append(s)
            endHeap.append(e)

        heapq.heapify(startHeap)
        heapq.heapify(endHeap)

        res = [0 for _ in people]
        count = 0

        peopleWithIndex = [
            (pTime, originalIdx)
            for originalIdx, pTime in enumerate(people)
        ]
        
        peopleWithIndex.sort()
        for pTime, idx in peopleWithIndex:
            while startHeap and startHeap[0] <= pTime:
                heapq.heappop(startHeap)
                count += 1

            while endHeap and endHeap[0] < pTime:
                heapq.heappop(endHeap)
                count -=1

            res[idx] = count

        return res
    
arr = [
    [
        [[1,6],[3,7],[9,12],[4,13]],
        [2,3,7,11],
    ],
    [
        [[1, 10], [3, 3]],
        [3, 3, 2],
    ]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.fullBloomFlowers(foo, bar)
print(res)