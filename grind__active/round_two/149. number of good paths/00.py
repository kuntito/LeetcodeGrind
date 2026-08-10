from typing import List

class Node:
    def __init__(self, nodeId, value):
        self.nodeId = nodeId
        self.value = value
        self.edges = []
        
    def __repr__(self):
        # return f'{self.nodeId} => {self.value}'
    
        edgeIds = ','.join([str(e.nodeId) for e in self.edges])
            
        return f'{self.nodeId} => ({edgeIds}))'

class Solution:
    def numberOfGoodPaths(
        self,
        vals: List[int],
        edges: List[List[int]]
    ) -> int:
        # construct the graph
        self.graph = self.constructGraph(vals, edges)
        
        print(2)
        
        
    def addNodeIfNotExist(self, nodeId, nodeVal, graph):
        if nodeId in graph: return
        
        node = Node(
            nodeId=nodeId,
            value=nodeVal,
        )
        
        graph[nodeId] = node
        
        
    def constructGraph(self, vals, edges):
        graph = {}
        for idNodeOne, idNodeTwo in edges:
            self.addNodeIfNotExist(idNodeOne, vals[idNodeOne], graph)
            self.addNodeIfNotExist(idNodeTwo, vals[idNodeTwo], graph)
            
            nodeOne = graph[idNodeOne]
            nodeTwo = graph[idNodeTwo]
            
            nodeOne.edges.append(nodeTwo)
            nodeTwo.edges.append(nodeOne)
            
        return graph


arr = [
    [
        [1,3,2,1,3],
        [[0,1],[0,2],[2,3],[2,4]],
    ],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.numberOfGoodPaths(foo, bar)
# print(res)