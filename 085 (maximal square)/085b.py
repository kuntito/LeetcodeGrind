# https://leetcode.com/problems/maximal-square/description/

# TODO explore this idea properly
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        pass
        # iterate through the grid for every position with `1`
        # using bfs, explore the right, downRight and down neighbours
        # if they are all 1's increase the level of the square
        
        res = 0
        for ri, row in enumerate(matrix):
            for ci, val in enumerate(row):
                if val == '1':
                    count = self.explore_square(ri, ci, matrix)
                    res = max(res, count)
                    
        return res ** 2
    
    def explore_square(self, start_ri, start_ci, matrix):
        pass
        pos = (start_ri, start_ci)
        level = 1
        seen = set()
    
        arr = [pos]
        seen.add(pos)
        
        while arr:
            tmp = []
            while arr:
                # coordinates of a valid position
                currPos = arr.pop()
                foo = self.explore_valid_neighbours(currPos, matrix, seen)
                if not foo:
                    return level
                
                tmp.extend(foo)
                    
            arr = tmp
            level += 1
            
        return level
    
    # TODO only add neighbours that have not been seen
    def explore_valid_neighbours(self, pos, matrix, seen):
        ri, ci = pos
        rows, cols = len(matrix), len(matrix[0])
        
        neis = [
            (ri, ci + 1),
            (ri + 1, ci + 1),
            (ri + 1, ci),
        ]

        for ni in neis:
            r, c = ni
            if r < 0 or r == rows or c < 0 or c == cols or matrix[r][c] == '0':
                return
            if ni in seen:
                pass
            
        return neis
                    
                
    
    
    
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