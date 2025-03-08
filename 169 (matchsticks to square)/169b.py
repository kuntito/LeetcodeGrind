# https://leetcode.com/problems/matchsticks-to-square/description/

class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        pass
    
        length = sum(matchsticks) // 4
        sides = [0] * 4
        
        if sum(matchsticks) / 4 != length:
            return False
        
        matchsticks.sort(reverse=True)
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        
        return backtrack(0)



arr = [
    [1,1,2,2,2],
]
foo = arr[-1]
sol = Solution()
res = sol.makesquare(foo)
print(res)