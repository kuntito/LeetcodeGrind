# https://leetcode.com/problems/kill-process/description/

from collections import defaultdict


class Solution:
    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        pass
        # we are given two arrays, `pid` and `ppid` that represent a process structure, let's rename them `foo` and `bar`
        
        # every element in foo, or rather foo[i] is the id of the ith process
        # and bar[i] is the id of the ith process's parent
        
        # so foo[i] represents a process
        # bar[i] is the id of it's parent
        
        # hence, bar contains parent nodes
        # it's giving graph, using this info, we can create a graph of processes
        
        # we're told the process with id==0, is the root process
        # once we have the graph, we can proceed, the idea here is that we're given an id, `kill`
        
        # it represents a node, we want to kill the process at that node
        # but what happens when we kill a process is all the child processes also die with it.
        
        # so there you go,
        
        # i'd suggest using a default dict
        # you want to create all the parent nodes first
        # the elements would be an array
        # then iterate through the child processes and place them in their appropriate parents
        
        # keep track of the kill node
        # so we don't have to traverse the entire graph to find it
        
        # once we have this we run a dfs through the kill node
        # and grab all the ids of the child nodes
        
        graph = defaultdict(list)
        
        for parent in ppid:
            graph[parent] = []
            
        for idx, child in enumerate(pid):
            parent = ppid[idx]
            graph[parent].append(child)
            
        res = []
        self.explore(kill, graph, res)
        
        return res
    
    def explore(self, node, graph, res):
        res.append(node)
        
        for nei in graph[node]:
            self.explore(nei, graph, res)
            
        
arr = [
    [[1,3,10,5], [3,0,5,3], 5],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.killProcess(foo, bar, baz)
print(res)