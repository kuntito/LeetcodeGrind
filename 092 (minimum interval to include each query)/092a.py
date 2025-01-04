# https://leetcode.com/problems/minimum-interval-to-include-each-query/description/

class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        pass
        # sort `intervals`
        intervals.sort()
        # you need a way to grab all intervals <= `query[j]`
        # to do this, find the index where `query[j] + 1` would exist
        # use binary search to find the target idx, `tgtIdx`
    
    
        res = []    
        for idx, q in enumerate(queries):
            # since intervals array is sorted, every interval from `tgtIdx` downwards
            # has a start less than `query[j]`
            tgtIdx = self.find_index(intervals, q + 1)
            
            val = self.find_interval(tgtIdx-1, intervals, q)
            res.append(val)            
        
        
            # iterate downwards and save the first interval size
            # who matches the condition `lefti <= queries[j] <= righti`
            
            # if none exists, return -1
            
        return res

    def find_interval(self, start_idx, intervals, target):
        min_size = None
        
        for idx in range(start_idx, -1, -1):
            val = intervals[idx]
            start, end = val
            
            if target <= end:
                size = end - start + 1
                if min_size is None:
                    min_size = size
                else:
                    min_size = min(
                        size,
                        min_size
                    )
            
        return -1 if min_size is None else min_size
    
    
    def find_index(self, arr, target):
        left, right = 0, len(arr)-1
        
        while left <= right:
            mid = (left + right) // 2
            
            midValue = arr[mid][0]
            if midValue == target:
                return mid
            elif target > midValue:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
        
arr = [
    [[[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]],
    [[[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minInterval(foo, bar)
print(res)