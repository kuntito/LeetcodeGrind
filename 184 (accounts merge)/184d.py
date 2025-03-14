# https://leetcode.com/problems/accounts-merge/description/

from collections import defaultdict
# for each set of mails, create an adjacency list
class Solution:
    def __init__(self):
        self.visited = set()
        self.adjacent = defaultdict(list)

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # Build adjacency list
        for account in accounts:
            first_email = account[1]
            for other_email in account[2:]:
                self.adjacent[first_email].append(other_email)
                self.adjacent[other_email].append(first_email)
                
        # at this point `self.adjacent` is a hashmap where each mail points to a list of mails it can reach

        merged_accounts = []
        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email not in self.visited:
                merged_account = [name]
                self.explore(merged_account, first_email)
                merged_account[1:] = sorted(merged_account[1:])  # Sort emails
                merged_accounts.append(merged_account)

        return merged_accounts


    def explore(self, merged_account, email):
        self.visited.add(email)
        merged_account.append(email)

        for neighbor in self.adjacent[email]:
            if neighbor not in self.visited:
                self.explore(merged_account, neighbor)


        
arr = [
    [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]],
    [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
]
foo = arr[-1]
sol = Solution()
res = sol.accountsMerge(foo)

for it in res:
    print(it)

