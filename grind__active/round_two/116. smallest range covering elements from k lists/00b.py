from typing import List


# TODO it works but there has to be cleaner solution.
# rewrite.
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pass
        flattenedNums = []
        numToRowIndexMap = {}
        
        for rowIdx, row in enumerate(nums):
            for n in row:
                flattenedNums.append(n)
                
                if n not in numToRowIndexMap:
                    numToRowIndexMap[n] = set()
                    
                numToRowIndexMap[n].add(rowIdx)


        flattenedNums.sort()
        # print(flattenedNums)
        
        # what would the sliding window look like?
        # it would be a hashmap of seen row indices
        # for each number in `flattenedNums`, we'd append it's row indices
        # to the sliding window, the moment len(slidingWindow) == rowCount,
        # we know we have a valid range
        # and how do we determine the range?
        # we'd have a start index
        # together with `idx`, we'd have the range (startIdx, idx)
        # then we save the range as the current smallest.
        
        # then move the start index forward until the slidingWindow is no longer valid
        # at which point, we proceed with `idx` and repeat the operation.
        
        # whenever i see a smaller range, i update what i've stored as smallest range.
        slidingWindow = {}
        startIdx = 0
        rowCount = len(nums)
        smallestRange = None
        
        for idx, n in enumerate(flattenedNums):
            # so what do i want to do
            # i want to grab the row indices for this number and insert into sliding window
            
            for rowIdx in numToRowIndexMap[n]:
                slidingWindow[rowIdx] = slidingWindow.get(rowIdx, 0) + 1
                
            while len(slidingWindow) == rowCount:
                numAtStart = flattenedNums[startIdx]
                numHere = flattenedNums[idx]
                
                newRange = (numAtStart, numHere)
                newRangeSize = numHere - numAtStart
                
                if newRangeSize == 0:
                    # you can't get a smaller range size than `0`
                    return newRange
                
                if smallestRange is None:
                    smallestRange = newRange
                else:
                    storedSize = smallestRange[1] - smallestRange[0]
                    if newRangeSize < storedSize:
                        smallestRange = newRange
                        
            
                self.removeIndicesFromWindow(
                    startIdx,
                    slidingWindow,
                    flattenedNums,
                    numToRowIndexMap
                )
                
                startIdx += 1
                
                
        return smallestRange
                
    def removeIndicesFromWindow(
        self,
        idx,
        slidingWindow,
        flattenedNums,
        rowIndicesMap,
    ):
        num = flattenedNums[idx]
        
        for ri in rowIndicesMap[num]:
            slidingWindow[ri] -= 1
            
            if slidingWindow[ri] == 0:
                del slidingWindow[ri]
        
            
            
arr = [
    [
        [1,2,3],
        [1,2,3],
        [1,2,3]
    ],
    [
        [4,10,15,24,26],
        [0,9,12,20],
        [5,18,22,30]
    ]
]
foo = arr[-1]
sol = Solution()
res = sol.smallestRange(foo)
print(res)