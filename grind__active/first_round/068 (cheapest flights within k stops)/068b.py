# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

# TODO https://neetcode.io/solutions/cheapest-flights-within-k-stops
# 19:51
import heapq

# TODO why does this work?
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        inf = float("inf")

        # each index in `prices` represents a flight
        prices = [inf] * n
        prices[src] = 0

        # `prices` does two things:
        #   initially, it tells you which nodes have not been visited by intializing them with `inf`
        #   unvisited nodes have a value that's != `inf`
        
        #   `prices[src] = 0` initalizes the starting position, indicating the first node has been visited
        #   and the cost of visiting the first node is `0`
        
        # cycle through every destination
        # every unvisited node `prices[nodeIdx] != inf` visits all it's neighbours
        # `prices[i]` effectively stores the shortest distance to node `i` so far
        
        for i in range(k + 1):
            # the reason for cloning prices is to maintain the records of unvisited nodes, since unvisited nodes could have their values changed...
            
            # TODO deep this explanation and implement your version
            tmpPrices = prices.copy()
            # for each destination,
            for source, destination, price in flights:
                # 'inf' represents unvisited stops
                # `prices[src] = 0` means only the start has been visited
                if prices[source] == inf:
                    continue
                print(i, source)
                
                cost = prices[source] + price
                tmpPrices[destination] = min(
                    tmpPrices[destination],
                    cost,
                )
                    
            # print(f'({i})', prices)
            # print(f'({i})', tmpPrices)
            print('*******************')
            prices = tmpPrices

        return -1 if prices[dst] == inf else prices[dst]
    
arr = [
    [[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1],
]
flights, src, dst, k = arr[-1]
sol = Solution()
res = sol.findCheapestPrice(len(flights), flights, src, dst, k)

print(res)
        
    