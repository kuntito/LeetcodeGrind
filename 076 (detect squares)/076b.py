# https://leetcode.com/problems/detect-squares/description/
from collections import defaultdict

# TODO deep solution
# https://www.desmos.com/calculator/epz8c47yk1
class DetectSquares:
    def __init__(self):
        pass
        self.ptsCount = defaultdict(int)
        self.all_pts = []


    def add(self, point) -> None:
        point = tuple(point)
        
        self.ptsCount[point] += 1
        self.all_pts.append(point)


    def count(self, point) -> int:
        res = 0
        px, py = point
        for x, y in self.all_pts:

            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res
    

sol = DetectSquares()
# sol.add([123, 8])
# sol.add([321, 8])
# sol.add([32, 38])
# sol.count([12, 18])
sol.add()
