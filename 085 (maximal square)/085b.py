# https://leetcode.com/problems/maximal-square/description/

# TODO https://neetcode.io/solutions/maximal-square
# 08:38
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        pass
        # iterate through the grid for every position with `1`
        # using bfs, explore the right, downRight and down neighbours
        # if they are all 1's increase the level of the square
        

        rows, cols = len(matrix), len(matrix[0])
        
        res = 0
        for ri, row in enumerate(matrix):
            for ci, val in enumerate(row):
                if val == '1':
                    foo = self.explore((ri, ci), matrix)
                    res = max(
                        res,
                        foo
                    )
        
        return res ** 2
    
    
    def explore(self, og, matrix):
        pass
        arr = [og]
        rows, cols = len(matrix), len(matrix[0])
        
        level = 1
        while arr:
            # location for next set of positions to explore
            seen = set()
            for pos in arr:
                ri, ci = pos
                neighbours = (
                    (ri, ci + 1),
                    (ri + 1, ci + 1),
                    (ri + 1, ci),
                )
                
                for nei in neighbours:
                    r, c = nei
                    if r < 0 or r == rows or c < 0 or c == cols or matrix[r][c] == '0':
                        return level
                    
                    if nei in seen: continue
                    seen.add(nei)
                  
            arr = seen  
            level += 1
            
        return level
                
    
    
    
arr = [
    [
        ["0","0","0","1"],
        ["1","1","0","1"],
        ["1","1","1","1"],
        ["0","1","1","1"],
        ["0","1","1","1"]
    ],
    [["0"]],
    [
        ["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
        ["1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","0","0","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","0","0","0","1","1","0","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","0","1","0","1","1","1","1","1","1","1","1"],
        ["1","1","1","0","0","1","0","1","1","1","1","1","1","1","1","1"],
    ],
    # [
    #     ["0","1"],
    #     ["1","0"]
    # ],
    # [
    #     ["1","0","1","0","0"],
    #     ["1","0","1","1","1"],
    #     ["1","1","1","1","1"],
    #     ["1","0","0","1","0"]
    # ],
    # [
    #     ["1","0","1","0","0"],
    #     ["1","0","1","1","1"],
    #     ["1","1","1","1","1"],
    #     ["1","0","0","1","0"]
    # ],
]


foo = arr[-1]
sol = Solution()
res = sol.maximalSquare(foo)
print(res)