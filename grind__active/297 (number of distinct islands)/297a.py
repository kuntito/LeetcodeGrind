# https://leetcode.com/problems/number-of-distinct-islands/description/

from collections import defaultdict


class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        pass
        # we're given a grid that contains 0's and 1's
        # the 1s represent land, the 0s represent water
        # a group of 1s connected horizontally or vertically represent an island

        # our job is to find distinct islands
        # two islands are similar if they have the same structure
        # i.e. same number of rows, and same number of columns on each row

        # i think an island can be identified by it's number of rows and the columns on each row
        # so we need a way to determine the id of an island

        # once we have this, we can tell if a new island is distinct
        # and count the frequency of distinct islands

        # but first, how do we determine an island
        # whenever, we find a 1, we explore for other vertical or horizontal 1s
        # we use a set to track all the one's we've found, or better still
        # modify the grid and convert to 0

        # but we also need to track the row and column of each one
        # how about our exploration takes row idx, and column idx
        # the exploration would always go right or down

        # we can use a hashmap for every unique row, it's value should be the an array that contains the number of columns on each row

        # with this we can extract the number of rows
        # "rowCount-colCountOne, colCountTwo"
        # save in a string of distinct islands, return len(distinctIslands)

        # first, iterate through the grid, find a 1

        distinctIslands = set()
        for ri, row in enumerate(grid):
            for ci, val in enumerate(row):
                if val == 1:
                    islandTracker = defaultdict(list)
                    self.explore(ri, ci, grid, islandTracker)
                    # parse island id
                    islandId = self.getIslandId(islandTracker)
                    # print(islandId)
                    # add island id to distinctIslands
                    distinctIslands.add(islandId)
                    
                    # for row in grid:
                    #     print(row)

                    
        return len(distinctIslands)

    # your process for identifying an island is flawed
    # consider edge cases, what does it mean to id an island
    # you can have two columns on the first row of an island
    # but different lengths between them, in that case, the islands are no longer the same, even though the id, says otherwise.
    def getIslandId(self, islandTracker):
        rowCount = len(islandTracker)
        sortedRows = sorted(islandTracker.keys())

        colsPerRow = []
        for ri in sortedRows:
            colsOnRow = str(len(islandTracker[ri]))
            colsPerRow.append(colsOnRow)

        colsConcat = ",".join(colsPerRow)
        return f"{rowCount}-{colsConcat}"

    def explore(self, ri, ci, grid, islandTracker):
        # determine the dimensions of the grid to check for out of bounds indices
        rows, cols = len(grid), len(grid[0])
        if ri < 0 or ri == rows or ci < 0 or ci == cols:
            return
        if grid[ri][ci] == 0:
            return

        islandTracker[ri].append(ci)
        
        # set that position to 0
        grid[ri][ci] = 0

        # now we go up, down, left, right
        self.explore(ri - 1, ci, grid, islandTracker)
        self.explore(ri + 1, ci, grid, islandTracker)
        self.explore(ri, ci + 1, grid, islandTracker)
        self.explore(ri, ci - 1, grid, islandTracker)


arr = [
    [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]],
    [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]],
    [
        [1,0,1],
        [1,1,1]
    ],
]
foo = arr[-1]
sol = Solution()
res = sol.numDistinctIslands(foo)
print(res)
