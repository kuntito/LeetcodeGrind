# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        pass
        # maintain a stack where each item is `(rectIdx, itemHeight)`
        # `rectIdx` is the start of that item's rectangle
        
        # for each new idx, the `rectHeight` is it's current idx unless
        # the previous item's value is greater than it's value
        
        # if the prevItem value is greater than currentItemValue,
        # `rectIdx` becomes the same as `previousValuesRectIx`
        
        # preValue is popped from the stack
        # and it's max area is calculated as it's height * (currIdx - prevValueRectIdx)
        
        maxArea = 0
        stack = []
        
        for idx, h in enumerate(heights):
            rectIdx = idx
            
            while stack and stack[-1][1] > h:
                prevRectIdx, preValue = stack.pop()
                maxArea = max(
                    maxArea,
                    preValue * (idx - prevRectIdx)
                )
                rectIdx = prevRectIdx
            
            stack.append((rectIdx, h))
        
        for rectIdx, value in stack:
            maxArea = max(
                maxArea,
                (len(heights) - rectIdx) * value
            )
            
        return maxArea
        
arr = [
    [2,1,5,6,2,3],
    [2, 4],
    [4,7,5,1,8,9,4,4,1,3,5,3,7,9,9,1,4],
    [4,2,0,3,2,4,3,4],
    [2,0,2],
]
foo = arr[-1]
sol = Solution()
res = sol.largestRectangleArea(foo)
print(res)
        