from typing import List

# a make shift solution to the idea at the end of b.py
# it runs infinitely, find out why..
# TODO
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candyCount = [0 for _ in ratings]

        for idx, rat in enumerate(ratings):
            self.explore(idx, ratings, candyCount)

        return sum(candyCount)

    def explore(self, idx, ratings, candyCount):
        if candyCount[idx] > 0: return

        curRat = ratings[idx]

        hasLeft = idx - 1 >= 0
        hasRight = idx < len(ratings)

        if hasLeft and candyCount[idx - 1] == 0:
            self.explore(idx - 1, ratings, candyCount)

        if hasRight and candyCount[idx + 1] == 0:
            self.explore(idx + 1, ratings, candyCount)

        curCount = 1
        if hasLeft and ratings[idx - 1] < curRat:
            curCount = candyCount[idx - 1] + 1

        if hasRight and ratings[idx - 1] < curRat and curCount <= candyCount[idx + 1]:
            curCount = candyCount[idx + 1] + 1

        candyCount[idx] = curCount
            
            
arr = [
    [1, 0, 2],
]
foo = arr[-1]
sol = Solution()
res = sol.candy(foo)
print(res)
            