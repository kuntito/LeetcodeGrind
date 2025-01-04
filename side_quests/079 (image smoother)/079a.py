# https://leetcode.com/problems/image-smoother/description/
import math

# TODO https://neetcode.io/solutions/image-smoother
class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        pass
        rows, cols = len(img), len(img[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]

    
        for ri, row in enumerate(img):
            for ci, _ in enumerate(row):
                avg = self.get_average(ri, ci, img)
                res[ri][ci] = avg
                
        return res
    
    def get_average(self, ri, ci, img):
        grid_cells = self.get_neighbours(ri, ci, img)
        
        total = sum(img[r][c] for r, c in grid_cells)
        count = len(grid_cells)
        return math.floor(total/count)
    
    
    def get_neighbours(self, start_ri, start_ci, arr):
        rows, cols = len(arr), len(arr[0])
        res = []
        for ri in range(start_ri - 1, start_ri + 2):
            for ci in range(start_ci-1, start_ci + 2):
                if ri >= 0 and ri < rows and ci >= 0 and ci < cols:
                    res.append((ri, ci))
                    
        return res
    
arr = [
    [[100,200,100],[200,50,200],[100,200,100]],
]
foo = arr[-1]
sol = Solution()
res = sol.imageSmoother(foo)

for r in res:
    print(r)