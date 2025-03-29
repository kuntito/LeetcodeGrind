# https://leetcode.com/problems/minimum-interval-to-include-each-query/description/
import heapq

# https://neetcode.io/solutions/minimum-interval-to-include-each-query
# 04:52
# TODO deep the solution
# TODO how does it compare to your binary search idea?
class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        pass
        # sort the intervals
        intervals.sort()
        
        # sort the queries
        sorted_queries = sorted(queries)
        
        minHeap = []
        res = {}
        
        i = 0 # this represents the index of the first interval
        for q in sorted_queries:
            # while the interval idx is valid and the intervals left is 
            # less than or equal to query, it means the query can exist in that interval
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
            
        return [res[q] for q in queries]
        
arr = [
    [[[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]],
    [[[4,5],[5,8],[1,9],[8,10],[1,6],[7,9],[3,3],[3,5],[1,6],[7,7]], [2,2,6,3,9,6,1,1,1,9]],
    [[[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minInterval(foo, bar)
print(res)