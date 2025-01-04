# https://leetcode.com/problems/maximal-square/description/

# TODO explore this idea properly
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        pass
        # iterate through the grid for every position with `1`
        # explore it with bfs
        # for each position, get all it's neighbours (right, downRight and down)
        # use a set to keep it unique
        # if the values of it's neighbours are all `1`
        # increment the square count
    
        res = 0
        for ri, row in enumerate(matrix):
            for ci, val in enumerate(row):
                if val == '1':
                    res = max(res, self.explore(ri, ci, matrix))

                    
        return res ** 2
    
    
    def explore(self, ri, ci, matrix):
        pass
        count = 1
    
        pos = (ri, ci)
        arr = [pos]
        
        while arr:
            seen = set()
            while arr:
                foo = arr.pop()
                neis = self.get_neighbours(foo, matrix)
                if len(neis) != 3:
                    return count
                for n in neis:
                    seen.add(n)
            
            arr = list(seen)
            count += 1
            
        return count
    
    
    def get_neighbours(self, pos, matrix):
        ri, ci = pos
        rows, cols = len(matrix), len(matrix[0])
        
        neis = [
            (ri, ci + 1),
            (ri + 1, ci + 1),
            (ri + 1, ci),
        ]
        
        return [(r, c) for r, c in neis if r >= 0 and r < rows and c >= 0 and c < cols and matrix[r][c] == '1']
    
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
    ], # TODO should be `64` not `49`
    [
        ["0","1"],
        ["1","0"]
    ],
    # [
    #     ["1","0","1","0","0"],
    #     ["1","0","1","1","1"],
    #     ["1","1","1","1","1"],
    #     ["1","0","0","1","0"]
    # ],
    [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
]


foo = arr[-1]
sol = Solution()
res = sol.maximalSquare(foo)
print(res)