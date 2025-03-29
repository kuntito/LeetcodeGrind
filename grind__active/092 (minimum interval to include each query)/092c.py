# https://leetcode.com/problems/minimum-interval-to-include-each-query/description/
import heapq


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        pass
        # for each query, we want to find the smallest interval that contains the query
        # if we sort the intervals by their right value
        # we know the query should be at most `rightValue`
        # since the values are sorted, we can use binary search to find `query`
        # we'd check based on the right value
        # we would either find the value or find it's insertion point
        
        # the edge case is what if there are multiple right values
        # i.e. query is `3`
        # and you have [1, 3], [2, 3], [3, 3]
        # the binary search would pick [2, 3] as the answer even though it's not
        # how about sort `intervals` based on right value pair
        
        # then create an array of unique end intervals, `uniques`
        # then we'd search this array for `query` or it's insertion point
        # if it's the insertion point we find, it's representation in intervals
        # would be `uniques[idx - 1]`

        
arr = [
    [[[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]],
    [[[4,5],[5,8],[1,9],[8,10],[1,6],[7,9],[3,3],[3,5],[1,6],[7,7]], [2,2,6,3,9,6,1,1,1,9]],
    [[[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minInterval(foo, bar)
print(res)