# https://leetcode.com/problems/network-delay-time/description/
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = {}
        # add all nodes to adjacency list
        for foo in range(1, n + 1):
            adj[foo] = []

        # add neighbours to nodes
        for start, dest, time in times:
            adj[start].append(
                (dest, time)
            )

        shortestPath = {}
        minHeap = [(0, k)]
        while minHeap:
            dist, node = heapq.heappop(minHeap)

            if node in shortestPath:
                continue
        
            shortestPath[node] = dist

            for nei, nei_dist in adj[node]:
                new_dist = nei_dist + dist
                heapq.heappush(minHeap, (new_dist, nei))

        # print(shortestPath)
        del shortestPath[k]
        
        if shortestPath and len(shortestPath) == n-1:
            return max(shortestPath.values())
        
        return -1



arr = [
    [[[1, 2, 1], [2, 1, 3]], 2, 2],
    [[[1, 2, 1]], 2, 2],
    [[[1, 2, 1]], 2, 1],
    [[[2,1,1],[2,3,1],[3,4,1]], 4, 2],
]
foo, bar, jay = arr[-1]
sol = Solution()
res = sol.networkDelayTime(foo, bar, jay)
print(res)