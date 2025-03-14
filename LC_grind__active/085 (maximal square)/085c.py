# https://leetcode.com/problems/maximal-square/description/

# TODO https://neetcode.io/solutions/maximal-square
# 06:24
# TODO compare with 085b.py
# why did i think storing the value in each cell won't work?
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        pass
        # starting from the bottom right
        # explore each cell where the value is `1`
        # store the amount of squares you can get from that point onwards
        # and assign the value, `matrix[ri][ci] = explore(...)` 
        
        # for each subsequent cell 
        # if the value is `1`, do the same for it's right, downRight and down children
        # matrix[ri][ci] = min(right, downRight, down) + 1
        
        rows, cols = len(matrix), len(matrix[0])

        res = 0        
        for ri in range(rows - 1, -1, -1):
            for ci in range(cols-1, -1, -1):
                right = self.explore(ri, ci + 1, matrix)
                downRight = self.explore(ri + 1, ci + 1, matrix)
                down = self.explore(ri + 1, ci, matrix)
                
                val = int(matrix[ri][ci])
                
                matrix[ri][ci] = val + min(right, downRight, down) if val == 1 else 0
                res = max(
                    res,
                    matrix[ri][ci]
                )
        
        # for rw in matrix:
        #     print(rw)
        
        return res ** 2
        
        
    def explore(self, sri, sci, arr):
        rows, cols = len(arr), len(arr[0])
        if sri < 0 or sri == rows or sci < 0 or sci == cols:
            return 0
        
        return int(arr[sri][sci])

                
    
    
    
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
    [
        ["1","1","0","1"],
        ["1","1","0","1"],
        ["1","1","1","1"]
    ]
]


foo = arr[-1]
sol = Solution()
res = sol.maximalSquare(foo)
print(res)