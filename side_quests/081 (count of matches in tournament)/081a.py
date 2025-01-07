# https://leetcode.com/problems/count-of-matches-in-tournament/description/

#  TODO https://neetcode.io/solutions/count-of-matches-in-tournament
class Solution:
    def numberOfMatches(self, n: int) -> int:
        pass
        count = 0
        while n > 1:
            pass
            matches = n // 2
            count += matches
        
            n = matches + (1 if n % 2 else 0)
        
        return count

arr = [
    7,
    14,
]
foo = arr[-1]
sol = Solution()
res = sol.numberOfMatches(foo)
print(res)