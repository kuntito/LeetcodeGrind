# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/

class Solution:
    def totalMoney(self, n: int) -> int:
        pass
    
        dotw = 7
        monday = 0
        curr = 0
        
        res = 0
        # two iterators, `idx` which iterates up to `n`
        # and `i` which represents multiples of `7`
        i = 0
        for _ in range(n):
            # dayIdx = i % 7
            # when `dayIdx == 0`, `week[dayIdx] = week[dayIdx] + 1`
            dayIdx = i % dotw
            
            if dayIdx == 0:
                monday += 1
                curr = monday
            else:
                curr += 1
            
            res += curr

            i += 1
                 
        return res


arr = [
    4, 
    20,
    10,
]
foo = arr[-1]
sol = Solution()
res = sol.totalMoney(foo)
print(res)