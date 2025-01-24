# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# TODO look at the answer
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        pass
        
        # TODO at each idx, you want to know how far you can travel left
        # before hitting a value index with a lower height
        # and how far it can travel right before hitting an index with a lower height
        
        # two arrays, left_traverse and right_traverse
        # each index of `left_traverse` contains the index of the furthest value leftwards
        # that's >= the curr value

        # to memoize, you want to check if the next position has been explored
        # if yes, return the explored value
        
        
        # first, how do you store the explored value for each position
        # with memo, after exploring each position, store the left and right result as a tuple
        memo = [None for _ in heights]
        

        maxArea = 0
        for idx, h in enumerate(heights):
            left_idx = self.get_left(h, idx, heights, memo)
            right_idx = self.get_right(h, idx, heights, memo)
            
            dist = (right_idx - left_idx) + 1
            area = dist * h
            
            maxArea = max(area, maxArea)
            memo[idx] = (left_idx, right_idx)
            
        return maxArea


    def get_left(self, min_height, start_idx, heights, memo):
        idx = start_idx
        while idx - 1 >= 0 and heights[idx - 1] >= min_height:
            idx -= 1
            curr_pos = heights[idx]
            # to check the memo
            # if there is a next value
            # if the next value is equal to min_height
            # if the next value has been explored, return it's left index
            next_pos_idx = idx - 1
            next_pos = heights[next_pos_idx] if next_pos_idx >= 0 else None
            if next_pos and next_pos == min_height:
                return memo[next_pos_idx][0]
                
            
        return idx
    
    def get_right(self, min_height, start_idx, heights, memo):
        idx = start_idx
        dim = len(heights)
        
        while idx + 1 < dim and heights[idx + 1] >= min_height:
            idx += 1
            
            next_idx = idx + 1
            next_pos = heights[next_idx] if next_idx < dim else None
            if next_pos and next_pos == min_height and memo[next_idx]:
                return memo[next_idx][1]
            
        return min(idx, dim-1)
            
        
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
        