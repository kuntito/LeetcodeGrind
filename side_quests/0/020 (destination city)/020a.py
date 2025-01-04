# https://leetcode.com/problems/destination-city/description/

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        seen = set() 
        for origin, _ in paths:
            seen.add(origin)

        for _, destination in paths:
            if destination not in seen:
                return destination
            
arr = [
    [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]],
    [["B","C"],["D","B"],["C","A"]],
    [["A","Z"]],
]
foo = arr[-1]
sol = Solution()
res = sol.destCity(foo)

print(res)