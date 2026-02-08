class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
    def __repr__(self):
        return f'({self.val})'

def createNodes(edges: list[list[int]]):
    
    nodeGraph = {}
    # create all nodes
    dim = len(edges)
    for idx in range(dim):
        val = idx + 1
        nodeGraph[val] = Node(val)
    
    # add neighbors
    for idx, neis in enumerate(edges):
        
        nodeVal = idx + 1
        
        for neiVal in neis:
            nodeGraph[nodeVal].neighbors.append(
                nodeGraph[neiVal],
            )

    return nodeGraph

        
