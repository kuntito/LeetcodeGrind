# https://leetcode.com/problems/accounts-merge/description/

from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        pass
        # the idea is to create a hashmap
        # where each mail points to a list of mails that's connected to it
        
        adjacency = self.getAllAdjacency(accounts)
        
        seen = set()
        # then use dfs to explore all connected components and create the merges
        # since every mail knows every mail, it doesn't matter which mail i start from
        
        res = []
        for ac in accounts:
            name = ac[0]
            startMail = ac[1]
            
            if startMail in seen:
                continue
            
            connectedMails = []
            self.explore(startMail, connectedMails, adjacency, seen)
            
            res.append([name] + sorted(connectedMails))
            
        return res
    
    def explore(self, startMail, connectedMails, adjacency, seen):
        if startMail in seen:
            return
        seen.add(startMail)
        connectedMails.append(startMail)
        
        for neiMail in adjacency[startMail]:
            if neiMail in seen: continue
            self.explore(neiMail, connectedMails, adjacency, seen)
            
            
            
        
    def getAllAdjacency(self, accounts):
        adjacency = defaultdict(list)
        for ac in accounts:
            mails = ac[1:]
            self.getAdjacencyMailSet(mails, adjacency)
        return adjacency
            
                
    def getAdjacencyMailSet(self, mails, adjacency):
        dim = len(mails)
        for idx, m in enumerate(mails):
            for j in range(idx + 1, dim):
                anotherM = mails[j]
                
                adjacency[m].append(anotherM)
                adjacency[anotherM].append(m)
                
                
                
                

        
arr = [
    [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]],
    [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]],
    [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
]
foo = arr[-1]
sol = Solution()
res = sol.accountsMerge(foo)

for it in res:
    print(it)

