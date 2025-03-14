import heapq

class Solution:
    def kClosest(self, points: list, k: int) -> list:
        arr = [
            [(x*x + y*y), x, y] for x, y in points
        ]
        heapq.heapify(arr)

        res = []
        for _ in range(k):
            res.append(
                heapq.heappop(arr)[1:]
            )
        
        return res
    

sol = Solution()
points = [[3, 3], [5, -1], [-2, 4]]
k = 2

# sol = Solution()
# points = [[1, 3], [-2, 2]]
# k = 1

res = sol.kClosest(points, k)
print(res)