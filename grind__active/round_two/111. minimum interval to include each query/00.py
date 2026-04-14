# https://leetcode.com/problems/minimum-interval-to-include-each-query/

from typing import List

import heapq

# TODO rewrite cleanly.
class Solution:
    def minInterval(
        self, 
        intervals: List[List[int]],
        queries: List[int]
    ) -> List[int]:
        
        minHeap = []
        
        # i'm sorting in reverse, so i can pop the leading intervals as i iterate
        intervals.sort(reverse=True)
        
        queries = [(q, idx) for idx, q in enumerate(queries)]
        queries.sort()
        
        res = [-1 for _ in queries]
        
        for q, qIdx in queries:
            # while there's intervals and the leading one
            # in our case, the trailing one,
            # when that one's start is less than or equal to query
            while intervals and intervals[-1][0] <= q:
                start, end = intervals.pop()
                                
                size = end - start + 1
                heapq.heappush(
                    minHeap,
                    (size, end)
                )
                
            # pop from the min heap if it's tip end is less than query.
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
                
            # at this point, if a tip exists..
            # it's the smallest size and it's end exceeds or is equal to the query.
            queryRes = minHeap[0][0] if minHeap else -1
            res[qIdx] = queryRes
            
        return res
    
arr = [
    [        
        [[1,4],[2,4],[3,6],[4,4]],
        [2,3,4,5],
    ],
    [
        [[2,3],[2,5],[1,8],[20,25]],
        [2,19,5,22],
    ]
]
foo, bar = arr[-1]
sol = Solution()

res = sol.minInterval(foo, bar)
print(res)
            
            