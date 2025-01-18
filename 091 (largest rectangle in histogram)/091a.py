# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        pass
        
        # TODO at each idx, you want to know how far you can travel left
        # before hitting a value index with a lower height
        # and how far it can travel right before hitting an index with a lower height
        
        # two arrays, left_traverse and right_traverse
        # each index of `left_traverse` contains the index of the furthest value leftwards
        # that's >= the curr value
        dim = len(heights)
        self.left_traverse = [None for _ in range(dim)]
        self.right_traverse = [None for _ in range(dim)]
        
        # TODO, to memoize, everytime you go left or right,
        # store the minimum that has been through a particular index
        
        res = 0
        for idx, val in enumerate(heights):
            leftIdx = self.get_left(idx, heights, val)
            rightIdx = self.get_right(idx, heights, val)
            
            self.left_traverse[idx] = leftIdx
            self.right_traverse[idx] = rightIdx
        
            dist = rightIdx - leftIdx + 1
            res = max(
                res,
                dist * heights[idx]
            )
                    
        return res
    
        
    def get_left(self, start_idx, heights, min_val):
        idx = start_idx
        
        while idx - 1 >= 0 and heights[idx - 1] >= min_val:
            if heights[idx - 1] == min_val:
                return self.left_traverse[idx - 1]
            
            idx -= 1
            
        return idx
        
    def get_right(self, start_idx, heights, min_val):
        idx = start_idx
        while idx + 1 < len(heights) and heights[idx + 1] >= min_val:
            if heights[idx + 1] == min_val and self.right_traverse[idx + 1]:
                return self.right_traverse[idx + 1]
            idx += 1
            
        return idx
        

        
            
        
arr = [
    [2, 4],
    [2,1,2],
    [2,1,5,6,2,3],
    [4,7,5,1,8,9,4,4,1,3,5,3,7,9,9,1,4],
]
foo = arr[-1]
sol = Solution()
res = sol.largestRectangleArea(foo)
print(res)
        