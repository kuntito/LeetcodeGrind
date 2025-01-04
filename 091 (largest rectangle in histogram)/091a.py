# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        pass
        
        # TODO critique the rationale for the stacks
        # each idx in heights wants to know if there are any smaller indexes to it's left and to it's right
        
        
        

    def get_left(self, heights):
        dim = len(heights)
        left = [None] * dim
        
        smallest = (heights[0], 0)
        for idx in range(dim):
            if idx == 0:
                continue

            left[idx] = smallest
            
            val = heights[idx]
            if val <= smallest[0]:
                smallest = (val, idx)

        return left


    def get_right(self, heights):
        dim = len(heights)
        right = [None] * dim
        smallest = (heights[dim-1], dim-1)
        for idx in range(dim-1, -1, -1):
            if idx == dim - 1:
                continue
            
            val = heights[idx]
            right[idx] = smallest
            if val <= smallest[0]:
                smallest = (val, idx)

        return right
        
arr = [
    [2,1,5,6,2,3],
]
foo = arr[-1]
sol = Solution()
res = sol.largestRectangleArea(foo)
print(res)
        