class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self) -> str:
        neighbours = ', '.join([f'{nei.val}-{id(nei)}' for nei in self.neighbors])
        return f'({self.val}, {id(self)}, [{neighbours}])'
        # return f'({self.val})'

    def __repr__(self) -> str:
        return str(self)


class Solution(object):
    def cloneGraph(self, node: Node):
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None