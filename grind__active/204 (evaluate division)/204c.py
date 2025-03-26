# https://leetcode.com/problems/evaluate-division/description/

from collections import defaultdict
# TODO look at solution
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        pass
        # create weighted graph
        # weight is the result of a/b = res
        # a ->(w_res)-> b
        
        # also create the inverse relationship
        # b -> (1/w_res) -> a
        
        graph = self.getGraph(equations, values)
        
        # for each query, run bfs
        # run bfs from qNum -> qDen
        # track all the weights it took to get there
        # the bfs node would contain the value and the weights it took to reach there
        arr = []
        for top, bottom in queries:
            res = self.explore(top, bottom, graph)
            arr.append(res)
            
        return arr
    
    def explore(self, start, target, graph):
        pass
        # TODO implement this
        
                
    def getGraph(self, equations, values):
        graph = defaultdict[list]
        
        for eq, val in zip(equations, values):
            top, bottom = eq
            
            graph[top].append([bottom, val])
            graph[bottom].append([top, 1/val])
            
        return graph
            

arr = [
    [
        [["a","b"],["b","c"]],
        [2.0,3.0],
        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    ],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.calcEquation(foo, bar, baz)
print(res)
        
        
        