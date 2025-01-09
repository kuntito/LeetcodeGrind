# https://leetcode.com/problems/detect-squares/description/
from collections import defaultdict

# TODO deep solution
class DetectSquares:

    def __init__(self):
        pass
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: list[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: list[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res
    

sol = DetectSquares()
sol.add([123, 8])
sol.add([321, 8])
sol.add([32, 38])
sol.count([12, 18])
