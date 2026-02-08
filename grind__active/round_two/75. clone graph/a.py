# https://leetcode.com/problems/clone-graph/description/
from createNodes import createNodes, Node

from typing import Optional


# i got a graph and i want to clone it.
# what do i do..
# well, create every new node and connect them accordingly.

# okay, and how would this go?
# i'd explore every node..

# say i've got
# 1 => 2
# the nodes are bidirectional btw.

# it'd be a recursive call
# i'd start with `1`, create a clone of `1`
# then explore it..

# inside the explore function, i'd run through the neighbours of `1`
# creating the neighbour clones as they come..
# connecting the neighbour clones to the parent `1` clone..

# then for each neighbour, i'd explore it too repeating the same process
# we'd need to store the nodes we've seen though..
# so `set`

# 1 <-> 2 <-> 3 <-> 1 (the end 1 is the same as the starting 1, it's a circular graph)
# from the jump, i clone `1`
# then explore it.. 

# inside the exploration, i have `1` and it's clone
# i add the og `1` to seen
# the i check the neighbours
# i see 2, i create 2s clone
# and explore it..

# i'm inside 2, i add the og `2` to seen
# then i check the neighbours, i see `1`
# i see it's been `seen` so i skip it..

# i see 3, create it's clone
# explore 3 and it's clone
# inside this, i add 3 to seen

# then check it's neighbors, which are 1 and 2
# both are seen, so i avoid it.

# now i come back to 2, nothing more to see
# i go back to 1, now, here's where the problem lies..

# 1s next neighbor, after 2, is 3..
# but when exploring 2s neighbors, i already added 3 to seen

# so 1 is going to avoid this 3
# and the connection is never made..

# FIXME you don't need all that..
# keep the logic as is, if the node has been seen, don't explore
# but connect the clones

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        cloneNode = Node(node.val)
        seen = {}
        self.explore(node, cloneNode, seen)
        
        return cloneNode
    
    def explore(self, ogNode, ogCloneNode, seen):
        if ogNode in seen:
            return
        
        seen[ogNode] = ogCloneNode
        
        for neiNode in ogNode.neighbors:
            if neiNode in seen: 
                neiCloneNode = seen[neiNode]
            else:         
                neiCloneNode = Node(neiNode.val)
                
            ogCloneNode.neighbors.append(neiCloneNode)

            
            self.explore(neiNode, neiCloneNode, seen)
                
arr = [
    [
        [2,4],
        [1,3],
        [2,4],
        [1,3]
    ],
]
edges = arr[-1]

nodeGraph = createNodes(edges)
nodeOne = nodeGraph[1]

sol = Solution()
sol.cloneGraph(nodeOne)