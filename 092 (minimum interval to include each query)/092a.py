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
        memo_tgt = {}
        memo_query = {}
        for idx, q in enumerate(queries):
            # since intervals array is sorted, every interval from `tgtIdx` downwards
            # has a start less than `query[j]`
            tgtIdx = self.find_index(intervals, q + 1, memo_tgt)
            
            val = self.find_interval(tgtIdx-1, intervals, q, memo_query)
            res.append(val)            
        
        
            # iterate downwards and save the first interval size
            # who matches the condition `lefti <= queries[j] <= righti`
            
            # if none exists, return -1
            
        return res

    def find_interval(self, start_idx, intervals, target, memo):
        if target in memo:
            return memo[target]
        
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
            
        memo[target] = -1 if min_size is None else min_size
        return memo[target]
    
    
    def find_index(self, arr, target, memo):
        if target in memo:
            return memo[target]
        
        left, right = 0, len(arr)-1
        
        while left <= right:
            mid = (left + right) // 2
            
            midValue = arr[mid][0]
            if midValue == target:
                while mid-1 < len(arr) and arr[mid-1][0] == arr[mid][0]:
                    mid -= 1
                memo[target] = mid
                return memo[target]
            elif target > midValue:
                left = mid + 1
            else:
                right = mid - 1
                
        while left < len(arr) and left-1 < len(arr) and arr[left-1][0] == arr[left][0]:
            left -= 1
                
        memo[target] = left
        return memo[target]
        
arr = [
    [[[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]],
    [[[4,5],[5,8],[1,9],[8,10],[1,6],[7,9],[3,3],[3,5],[1,6],[7,7]], [2,2,6,3,9,6,1,1,1,9]],
    [[[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minInterval(foo, bar)
print(res)