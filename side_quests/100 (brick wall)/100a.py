# https://leetcode.com/problems/brick-wall/description/

# https://neetcode.io/solutions/brick-wall
class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        pass
        # to find the minimum number of crossed bricks
        # find the position with the most edges

        # for each row, determine all it's edges
        # which ever edge occurs the most
        # subtract it from the total number of rows
        
        hashmap = {}
        for row in wall:
            edge = 0
            # skip the last brick
            for brick in row[:-1]:
                edge += brick
                hashmap[edge] = hashmap.get(edge, 0) + 1
                


        most_edges = max(hashmap.values()) if hashmap.values() else 0
        return len(wall) - most_edges
        
        
arr = [
    [
        [1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]
    ],
    [[1],[1],[1]],
    [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
]
foo = arr[-1]
sol = Solution()
res = sol.leastBricks(foo)
print(res)