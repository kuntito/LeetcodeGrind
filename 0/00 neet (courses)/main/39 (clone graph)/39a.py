# https://leetcode.com/problems/clone-graph/description/

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

from collections import deque

class Solution(object):
    def cloneGraph(self, node: Node):
        if node is None:
            return node

        clone = Node(node.val)
        self.clone_map = {}
        self.clone_map[node] = clone


        self.queue = deque()
        self.queue.append(node)
        self.visited = set()

        self.explore_queue()

        return clone

    def explore_queue(self):
        queue = self.queue
        visited = self.visited
        clone_map = self.clone_map

        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                if node in visited: continue

                for nei in node.neighbors:
                    if nei in visited: continue
                    queue.append(nei)

                    nei_clone = clone_map[nei] if nei in clone_map else Node(nei.val)
                    clone_map[nei] = nei_clone

                    clone_parent = clone_map[node]
                    clone_parent.neighbors.append(nei_clone)
                    nei_clone.neighbors.append(clone_parent)

                visited.add(node)


one = Node(1)
two = Node(2)
four = Node(4)
three = Node(3)

one.neighbors.extend([two, four])
two.neighbors.extend([one, three])
four.neighbors.extend([one, three])
three.neighbors.extend([two, four])

sol = Solution()
res = sol.cloneGraph(one)

print(res)
