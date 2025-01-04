# https://leetcode.com/problems/maximal-square/description/

# TODO explore this idea properly
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        pass

        # iterate through the grid
        # for each position with `1`, declare a variable called `square count - = 1`
        # start a bfs
        # explore all UNIQUE right, down, and rightdown values
        # if they are all `1s`
        # increment the square count
        # else break the loop and return
        
        
        res = 0
        for ri, row in enumerate(matrix):
            for ci, val in enumerate(row):
                if val == '1':
                    res = max(res, self.explore(ri, ci, matrix))
                    
        return res

    
arr = [
    [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ],
    [
        ["0","1"],
        ["1","0"]
    ],
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
]


foo = arr[-1]
sol = Solution()
res = sol.maximalSquare(foo)
print(res)