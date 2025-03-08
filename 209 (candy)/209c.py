# https://leetcode.com/problems/candy/description/


class Solution:
    def candy(self, ratings: list[int]) -> int:
        pass
        # it looks like a topological sort problem
        # the leaf nodes are children with the least ratings
        
        dim = len(ratings)
        graph = {}
        for idx in range(dim):
            graph[idx] = []
            
        for idx in range(dim):
            prevRating = None if idx == 0 else ratings[idx - 1]
            nextRating = None if idx + 1 == dim else ratings[idx + 1]
            
            currRating = ratings[idx]
            if isinstance(prevRating, int) and currRating > prevRating:
                graph[idx].append(idx - 1)
            if isinstance(nextRating, int) and currRating > nextRating:
                graph[idx].append(idx + 1)

        candyAllocation = [0 for _ in ratings]
        # then explore the dependency graph in a post order manner
        # make sure every parent's rating is at least 1 OR equal max(leftChild, rightChild) + 1
        
        # print(graph)
        
        visited = set()
        for i in range(dim):
            self.explore(i, graph, candyAllocation, visited)
            
        return sum(candyAllocation)


    def explore(self, node, graph, candyAllocation, visited):
        pass
        if node in visited:
            return candyAllocation[node]
        
        visited.add(node)
        
        maxNei = 0
        for nei in graph[node]:
            maxNei = max(
                maxNei,
                self.explore(nei, graph, candyAllocation, visited)
            )
            
        candyAllocation[node] = maxNei + 1
        return candyAllocation[node]
        
        
    
    
arr = [
    [1, 0, 2],
    [1,2,87,87,87,2,1],
    [1, 2, 2],
]
foo = arr[-1]
sol = Solution()
res = sol.candy(foo)
print(res)