# https://leetcode.com/problems/clone-graph/description/
from createNodes import createNodes, Node

from typing import Optional


# i want to rewrite the function to use `node.val` as key
# what's the goal, clone a graph of bidirectional nodes.

# what's the approach, explore every node, creating a clone as you go
# and connecting the neighbors

# say you have 1 <-> 2
# and the starting node is `1`

# you create a clone of `1`
# and start a recursive call with `1` and it's clone

# inside the call, you explore `1`s neighbors
# in this case, it's only 2

# at this point, you clone 2
# and explore it the same way you did 1
# 2 and its clone

# you come in 2
# explore it's neighbors, this case, it's only 1..

# do you create 1 again.. no, because we've seen it.
# we simply add the 1s clone to 2s neighbors

# and we're done here..

# we'd need somewhere to store created clones
# that's where a hashmap comes in

# node.val => node

# TODO feel like there's a cleaner way to write this to avoid the not node check
        # if not node:
        #     return node
# look up official solution

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        seenMap = {}
        
        nodeClone = Node(node.val)
        self.explore(node, nodeClone, seenMap)
        
        return nodeClone
    
    def explore(self, ogNode, ogCloneNode, seenMap):
        if ogCloneNode.val in seenMap:
            return
            
        seenMap[ogCloneNode.val] = ogCloneNode
        
        for neiNode in ogNode.neighbors:
            neiCloneNode = seenMap[neiNode.val] if neiNode.val in seenMap else Node(neiNode.val)
            
            ogCloneNode.neighbors.append(neiCloneNode)
            self.explore(neiNode, neiCloneNode, seenMap)
            
                

                
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