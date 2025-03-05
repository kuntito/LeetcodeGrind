# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

from collections import deque
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        pass
        # at each index, you need to know the highest on it's left
        # and the highest on it's right
        
        # use a monotonically decreasing stack for the left
        # a monotonically increasing stack for the right
        # run the calculation and store the max
        
        # TODO the monotonic idea doesn't work
        # consider `[7, 3, 5]`
        # at index `2`, the stack would read [7, 5]
        # indicating that `7` is the left most largest
        # but that wouldn't be possible since `3` exists between them
        
        dim = len(heights)
        
        # use one array to store the left result
        # each idx's furthest left is initially itself
        leftHeights = [idx for idx in range(dim)]
        
        stack = []
        for idx, h in enumerate(heights):
            while stack and h > stack[-1][1]:
                stack.clear()
                
            stack.append((idx, h))
            # the furthest index to it's left
            leftHeights[idx] = stack[0][0]
            
            
        maxArea = 0
        queue = deque()
        # then while parsing from the right
        # calculate the rectangle and track the max
        for idx in range(dim-1, -1, -1):
            h = heights[idx]
            while queue and h > queue[0][1]:
                queue.clear()
                
            queue.appendleft((idx, h))
            # print(queue)
            
            rightIdx = queue[-1][0]
            leftIdx = leftHeights[idx]
            
            dist = (rightIdx - leftIdx) + 1
            area = dist * h
            
            # if area == 98:
            #     print(stack)
            #     print(idx, leftIdx, rightIdx)
            #     print(heights)
                        
            maxArea = max(
                maxArea,
                area
            )
        
        return maxArea
        
arr = [
    [2,1,5,6,2,3],
    [2, 4],
    [4,7,5,1,8,9,4,4,1,3,5,3,7,9,9,1,4],
]
foo = arr[-1]
sol = Solution()
res = sol.largestRectangleArea(foo)
print(res)
        