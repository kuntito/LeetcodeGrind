
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        self.rows, self.cols = len(obstacleGrid), len(obstacleGrid[0])
        self.grid = obstacleGrid

        self.pos_map = {(self.rows-1, self.cols-1): 1}
        return self.explorePos(0, 0)


    def explorePos(self, ri: int, ci: int):
        if ri == self.rows or ci == self.cols or self.grid[ri][ci]:
            return 0
        
        pos = (ri, ci)
        if pos not in self.pos_map:
            self.pos_map[pos] = self.explorePos(ri+1, ci) + self.explorePos(ri, ci+1)
        return self.pos_map[pos]