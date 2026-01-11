# https://leetcode.com/problems/minimum-interval-to-include-each-query/description/
import heapq

# TODO TLE
class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        pass
        # how about we sort `intervals` by length
        # the idea is to iterate through each interval range
        # and use a hashmap to track the numbers you've seen
        # i.e. [1, 3], [3, 8]
        # we'd go through 1, 2, 3 and store them in the hashmap as
        # 1 -> 3, 2 -> 3, 3 ->
        
        # then we explore the next interval [3, 8]
        # since `3` is in the hashmap and we've sorted intervals by length
        # it means this current interval cannot be shorter
        # therefore we skip three
        # and go through 4, 5, 6, 7, 8
        
        # rather than store all the values
        # convert query to a set
        
        # go thorugh each interval range
        # for any value in in query
        # add it to the hashmap and remove from queries set
        
        # if queries set becomes empty we go home
        
        
        querySet = set(queries)
        resMap = {}
        
        intervals.sort(key=lambda x: (x[1] + 1 - x[0]))
        for q in intervals:
            for n in range(q[0], q[1] + 1):
                if n in querySet:
                    resMap[n] = q[1] + 1 - q[0]
                    querySet.remove(n)
            if not querySet:
                break
            
        res = []
        
        for q in queries:
            if q in resMap:
                res.append(resMap[q])
            else:
                res.append(-1)
        
        return res
        
        
arr = [
    [[[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]],
    [[[4,5],[5,8],[1,9],[8,10],[1,6],[7,9],[3,3],[3,5],[1,6],[7,7]], [2,2,6,3,9,6,1,1,1,9]],
    [[[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minInterval(foo, bar)
print(res)