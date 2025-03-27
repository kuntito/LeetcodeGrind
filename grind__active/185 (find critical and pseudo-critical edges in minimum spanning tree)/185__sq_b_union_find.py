# https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        pass
        # the question states that the graph has one redundant edge
        # which means the graph nodes can stay connected if that edge is removed
        # what is this edge
        
        uf = UnionFind(edges)
        
        # this question naturally lends itself to union find
        for e in edges:
            if not uf.addEdge(e):
                return e
            
        
class UnionFind:
    def __init__(self, edges):
        self.parents = {}
        self.rank = {}
        # set every node to be it's own parent
        # set every rank to `1`
        for a, b in edges:
            if a not in self.parents:
                self.parents[a] = a
                self.rank[a] = 1
            
            if b in self.parents: continue
            self.parents[b] = b
            self.rank[b] = 1
        
    def addEdge(self, edge):
        pass
        a, b = edge
        # get the root parents of `a` and root parent of `b`
        root_a = self.get_root(a)
        root_b = self.get_root(b)
        
        
        # the the root parents happen to be the same
        # it means that edge has already been connected
        # in this case return `False`
        if root_a == root_b:
            return False
        
        # get the rank for each parent
        # connect the lesser to the larger
        # update the rank of the larger
        rank_a = self.rank[root_a]
        rank_b = self.rank[root_b]
        
        if rank_a > rank_b:
            self.join(alpha=root_a, beta=root_b)
        else:
            self.join(alpha=root_b, beta=root_a)
        
        return True
    
    def join(self, alpha, beta):
        alphaRank = self.rank[alpha]
        betaRank = self.rank[beta]
        
        self.parents[beta] = alpha
        if alphaRank == betaRank:
            self.rank[alpha] += 1
    
        
    def get_root(self, node):
        res = node
        while res != self.parents[res]:
            res = self.parents[res]
        
        return res
    

arr = [
    [[1, 2], [1, 3], [2, 3]],
    [[1,2],[2,3],[3,4],[1,4],[1,5]],
]
foo = arr[-1]
sol = Solution()
res = sol.findRedundantConnection(foo)

print(res)