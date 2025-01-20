# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        pass
        
        # create an adjacency list for flights
        adj_list = self.create_adjacency_list(flights)
    
        # the idea is to visit nodes in levels
        # starting from the first node, how many nodes can you reach?
        # store them, that's one stop
        # exploring from all the nodes reached from the first stop
        # how many other nodes can you reach, that's another stop
        # do this until the max stops is reached
        
        # use a hashmap to store each node and the minimum distance it takes to get there
        # this is initialized to float("inf"), the highest possible number
        hashmap = {}
        for i in range(n):
            hashmap[i] = float("inf")
            
        # initialize source to `0`, since it's the origin
        hashmap[src] = 0
        levels = k + 1
        
        candidates = [src]
        
        while levels:
            duplicate = hashmap.copy()
            nextCandidates = []
            # for each node in `candidates`
            while candidates:
                curr = candidates.pop()
                
                currPrice = hashmap[curr]
                for nei, neiPrice in adj_list[curr]:
                    # the price it takes to get from `curr` to `nei`
                    totalPrice = currPrice + neiPrice
                    if totalPrice < duplicate[nei]:
                        duplicate[nei] = totalPrice
                        
                        nextCandidates.append(nei)
                        
            hashmap = duplicate
            candidates = nextCandidates
            levels -= 1
            
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
    [[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], 0, 2, 2],
    [[[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1],
    [[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1],
    [[[1,2,4]], 0, 4, 2], # TODO, figure this out
]
flights, src, dst, k = arr[-1]
sol = Solution()
res = sol.findCheapestPrice(len(flights), flights, src, dst, k)

print(res)
        