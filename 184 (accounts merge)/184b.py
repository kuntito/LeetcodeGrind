# https://leetcode.com/problems/accounts-merge/

from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        emailIdx = {} # email -> id
        emails = [] # list of emails for all accounts
        emailToAcc = {} # email_index -> account_idx

        count = 0
        for accId, a in enumerate(accounts):
            # iterating from `1` onwards means each element in `a`
            # is an email
            for i in range(1, len(a)):
                email = a[i]

                if email in emailIdx:
                    continue
                
                emails.append(email)
                emailIdx[email] = count
                emailToAcc[count] = accId
                count += 1
        
        # the block above creates a list of all mails
        # it creates a hashmap that points every mail to a unique idx, `count`
        # another hashmap that points each mail idx, `count` to it's account idx
        
        
        # creates an empty list for all unique mails
        adj = [[] for _ in range(count)]
        
        for a in accounts:
            # it's creating undirected edges between every mail of a particular acount
            for i in range(2, len(a)):
                id1 = emailIdx[a[i]]
                id2 = emailIdx[a[i - 1]]
                adj[id1].append(id2)
                adj[id2].append(id1)
        
        
        print(adj)
        
        emailGroup = defaultdict(list)
        visited = [False] * count
        for i in range(count):
            if not visited[i]:
                self.explore(i, emailToAcc[i], visited, emailGroup, emails, adj)
        
        res = []
        for accId in emailGroup:
            name = accounts[accId][0]
            res.append([name] + sorted(emailGroup[accId]))
        
        return res
    
    
    def explore(self, node, accId, visited, emailGroup, emails, adj):
        visited[node] = True
        emailGroup[accId].append(emails[node])
        for nei in adj[node]:
            if not visited[nei]:
                self.explore(nei, accId, visited, emailGroup, emails, adj)
        
        
arr = [
    [
        ["John","johnsmith@mail.com","john_newyork@mail.com"],
        ["John","johnsmith@mail.com","john00@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]
    ],
]
foo = arr[-1]
sol = Solution()
res = sol.accountsMerge(foo)
