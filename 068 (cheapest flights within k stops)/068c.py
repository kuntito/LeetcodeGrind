# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

# TODO why does this cause a memory error?
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        pass
    
        # create a set for visited nodes
        # add the starting node, `src`
        visited = []
        visited.append(src)
        
        # create an adjacency list for flights
        adj_list = self.create_adjacency_list(flights)
        
        
        # create a hashmap for each node
        # hashmap = {node: shortest_distance_to_node}
        # initialize the shortest distance for each node to `float("inf")`
        hashmap = {}
        for i in range(n):
            hashmap[i] = float("inf")

        # set hashmap[0] = 0
        hashmap[src] = 0
        
        count = k + 1
        while visited and count:
            next_set = []
            newHash = hashmap.copy()
            
            while visited:
                currNode = visited.pop()
                for nei, neiPrice in adj_list[currNode]:
                    next_set.append(nei)
                    
                    currPrice = hashmap[currNode] + neiPrice
                    # FIXME i'm updating the hashmap with the newest values before visiting all the pending nodes
                    if currPrice < newHash[nei]:
                        newHash[nei] = currPrice
            # print(next_set)
            visited = next_set
            hashmap = newHash
            count -= 1
            
        return -1 if hashmap[dst] == float("inf") else hashmap[dst]
        
        
    def create_adjacency_list(self, flights):
        hashmap = {}
        
        for src, dst, price in flights:
            if src not in hashmap:
                hashmap[src] = []
            if dst not in hashmap:
                hashmap[dst] = []
                
            hashmap[src].append((dst, price))
            
        return hashmap
    
arr = [
    [[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1],
    [[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], 0, 2, 2],
]
flights, src, dst, k = arr[-1]
sol = Solution()
res = sol.findCheapestPrice(len(flights), flights, src, dst, k)

print(res)
        