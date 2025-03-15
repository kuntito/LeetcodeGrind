# https://leetcode.com/problems/accounts-merge/description/

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        pass
    
        # declare a set for visited indices, `seen`
        # a hashmap for each name => emails
        seen = set()
        hashmap = {}
    
    
        dim = len(accounts)
        # iterate through accounts with index
        for idx, azas in enumerate(accounts):
            # if index in seen: continue
            if idx in seen: continue
            name, mails = azas[0], azas[1:]
            
            # for each index
            # create a hashmap key from `f"{idx}_{name}"`
            # hashmap[key] = set()
            # add all it's emails to the set
            main_set = set(mails)

            # iterate through the indices (idx + 1, dim)
            for j in range(idx + 1, dim):
                # for each `j`, check all it's emails
                # if any email is in `hashmap[key]`
                # add all of the j's mails to `hashmap[key]`
                # add `j` to seen
                
                second_mails = accounts[j][1:]
                for mail in second_mails:
                    if mail in main_set:
                        seen.add(j)
                        for m in second_mails:
                            main_set.add(m)
                        break
                    
            key = f"{idx}_{name}"
            hashmap[key] = main_set
        
        # create `res`
        res = []
        # convert all sets to lists
        for key, sets in hashmap.items():
            # extract name, sort lists
            name = key.split("_")[1]
            lst = sorted(list(sets))
            
            # combine in a list, append to res
            res.append([name] + lst)
        
        
        return res

        
arr = [
    [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]],
    [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
]
foo = arr[-1]
sol = Solution()
res = sol.accountsMerge(foo)

for it in res:
    print(it)

