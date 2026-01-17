# https://leetcode.com/problems/path-with-minimum-effort/description/

from typing import List

# i can solve this joint with Dijkstra..

# the idea is you start at (0, 0)
# then add it's neighbours to a queue..
# each neighbour is a collection of two thing..
#     it's coordinates
#     it's effort, how much did it take to get from parent to neighbour..
#         it's occured to me, i'd need a minHeap not a queue..

# the idea is the minHeap always know the lowest effort path next..
# each heap node should be (effort, coordinates)
# this way on each exploration, we grab the next available minimum effort..

# we keep doing this till we hit destination..
# and at this point.. the first destination we reach has the minimum effort..
# the minHeap is what changes the game..

# perhaps, i could've gotten my approach to work but i couldn't find a way to write out my logic
# plus, it's less optimal. i wanted to explore every path to destination, tracking the max effort for each path
# then returning the minimum of those..

# Dijkstra's naturally handles both.. actually.. it naturally handles the minimum effort
# not tracking the maxEffort path..

# on each node.. i want to maintain the max Effort from it's parent..
# each neighbour nodes effort should be max(parentEffort, effort)
# this way each node knows the max effort it's seen so far..

# now, i can say Dijkstra naturally handles both.. 

# and how are we writing this, create minHeap
# add first node = (initEffort, (0, 0))
# `initEffort` should be `0`

# while minHeap has values..
# pop the topmost node from minHeap, this would be the next least effor path
# check if coordinates == finalDestination
# if yes, return effort

# else run through topmost nodes neighbours..
# for each neighbour, calculate neighbour effort..
# add neighbour to minHeap
# neighbour is (
#     max(neighbourEffor, topmostNodeEffort),
#     neighbourCoordinates
# )
# keep balling..

# one more thing, visited nodes..
# we don't handle them in the traditional sense of each path should go to what it's seen before
# rather the algorithm structure handles that..

# does it? i was going to say since, we're guaranteed to always pick the least effort node..
# if we store all visited nodes.. a general `seen` set, any time we hit those coordinates, we know
# the effort of that node is bound to be greater than the one we've seen

# it seems to make sense, let's implement this.. but big props to Dijkstra.. this joint solves
# multiple problems in one go.. who are these guys?
import heapq   
    
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pass
        minHeap = []
        rows, cols = len(heights), len(heights[0])
        finalDestination = (
            rows - 1,
            cols - 1,
        )
        
        origin = (0, 0)
        firstNode = (0, origin)
        
        seen = set()
        
        heapq.heappush(minHeap, firstNode)
        
        while minHeap:
            curEffort, curPos = heapq.heappop(minHeap)
            
            if curPos == finalDestination:
                return curEffort

            # initiallly submitted without this check and ran into TLE
            # the problem it solves is this.. 
            # grid:
            # 1 - 3
            # |   |
            # 2 - 5
            
            # when i explore the valid neighbours of 1, i'd get (2, 3)
            # at this point, `1` is in `seen`
            # i then pop and explore the neighbours..
            # the problem is minHeap would contain the valid neighbours of (2, 3)
            # at this point, meaning minHeap would contain `5` twice, hence.. (5, 5)
            
            # now when i get back to main iteration..
            # i'd only pop the lowest effort `5` but the second `5` still exists
            # but because of how Dijkstra is designed, i need not explore that position with `5`
            # again, hence, why i need to skip it here..
            
            # the seen in neighbours is still efficient.. in essence, it's saying don't add seen neighbours
            # the second check is ensuring, for nodes with the same position, we only check the one with the least effort, skip the rest
            
            if curPos in seen:
                continue
            
            seen.add(curPos)
            
            for neiPos in self.getNeighbours(curPos, seen, heights):
                neiEffort = self.getEffort(neiPos, curPos, heights)
                
                neiNode = (
                    max(
                        curEffort,
                        neiEffort,
                    ),
                    neiPos,
                )
                
                heapq.heappush(
                    minHeap,
                    neiNode
                )
                
    def getNeighbours(self, pos, seen, heights):
        r, c = pos
        
        neis = (
            (r - 1, c),
            (r + 1, c),
            (r, c - 1),
            (r, c + 1),
        )
        
        rows, cols = len(heights), len(heights[0])
        is_in_bounds = lambda a, b: a >= 0 and a < rows and b >= 0 and b < cols
        
        return [pos for pos in neis if pos not in seen and is_in_bounds(pos[0], pos[1])]

    
    def getEffort(self, posOne, posTwo, heights):
        rwOne, clOne = posOne
        rwTwo, clTwo = posTwo
        
        valOne = heights[rwOne][clOne]
        valTwo = heights[rwTwo][clTwo]
        
        return abs(valOne - valTwo)