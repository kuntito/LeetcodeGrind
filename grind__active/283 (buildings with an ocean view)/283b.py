class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:        
        # iterate rtl, keeping a monotonically descending stack
        # if the current height is greater than the topmost height
        # we have an index

        dim = len(heights)
        stack = []
        res = []
        for idx in range(dim-1, -1, -1):
            h = heights[idx]
            if not stack or h > stack[-1]:
                res.append(idx)
                stack.append(h)
        

        return res[::-1]