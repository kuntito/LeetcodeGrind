# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/

# TODO https://neetcode.io/solutions/calculate-money-in-leetcode-bank
class Solution:
    def totalMoney(self, n: int) -> int:
        pass
    
        dotw = 7
        week = [0] * dotw
        
        res = 0
        # two iterators, `idx` which iterates up to `n`
        # and `i` which represents multiples of `7`
        i = 0
        for _ in range(n):
            # dayIdx = i % 7
            # when `dayIdx == 0`, `week[dayIdx] = week[dayIdx] + 1`
            dayIdx = i % 7
            
            if dayIdx == 0:
                week[dayIdx] = week[dayIdx] + 1
            else:
                week[dayIdx] = week[dayIdx-1] + 1
            
            res += week[dayIdx]

            i += 1
                 
        return res


arr = [
    4,
    10,
    20,
]
foo = arr[-1]
sol = Solution()
res = sol.totalMoney(foo)
print(res)