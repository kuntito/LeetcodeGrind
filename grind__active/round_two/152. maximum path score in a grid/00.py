from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        self.grid = grid
        self.maxCost = k
        
        startPos = (0, 0)
        score, cost = self.explore(startPos)

        
        return score if cost <= k else -1
    
    def getCost(self, value):
        if value == 2:
            return 1
        
        return value
    
    def is_out_of_bounds(self, pos):
        ri, ci = pos
        rows, cols = len(self.grid), len(self.grid[0])
        
        return ri < 0 or ri >= rows or ci < 0 or ci >= cols
    
    def explore(self, startPos):
        if self.is_out_of_bounds(startPos):
            return None, None
        
        r, c = startPos
        scoreHere = self.grid[r][c]
        costHere = self.getCost(scoreHere)

        rows, cols = len(self.grid), len(self.grid[0])
        if r == rows - 1 and c == cols - 1:
            return scoreHere, costHere
        
        
        
        rightScore, rightCost = self.explore((r, c + 1))
        downScore, downCost = self.explore((r + 1, c))
        
        newScore, newCost = None, None
        if rightScore is not None:
            newScore = scoreHere + rightScore
            newCost = costHere + rightCost
    
        if downScore is not None:
            if newScore is None:
                newScore = scoreHere + downScore
                newCost = costHere + downCost
            else:
                has_better_score = (scoreHere + downScore) > newScore
                has_lower_cost = (costHere + downCost) < newCost
                
                if has_better_score:
                
                
        if newScore is None:
            return scoreHere, costHere
        
        return newScore, newCost
    
arr = [
    [
        [
            [0, 1],
            [1, 2]
        ],
        1
    ],
    [
        [
            [1],
            [2]
        ],
        1
    ],
]

foo, bar = arr[-1]


sol = Solution()
res = sol.maxPathScore(foo, bar)
print(res)