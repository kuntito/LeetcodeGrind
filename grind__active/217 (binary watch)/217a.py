# https://leetcode.com/problems/binary-watch/description/

from itertools import combinations

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        pass
        # it's a combination problem
        # in how many ways can you select `turnedOn` from `pool`
        # `pool` is all the possible LEDS
        
        pool = [
            [8, 'H'],
            [4, 'H'],
            [2, 'H'],
            [1, 'H'],
            [32, 'M'],
            [16, 'M'],
            [8, 'M'],
            [4, 'M'],
            [2, 'M'],
            [1, 'M'],
        ]
        
        subsets = combinations(pool, turnedOn)
        
        res = []
        for comb in subsets:
            parse_res = self.parse(comb)
            if parse_res:
                res.append(parse_res)
                
        return res
    
    def parse(self, comb):
        hours, minutes = 0, 0
        
        for dig, typ in comb:
            if typ == 'H':
                hours += dig
                if hours > 11:
                    return None
            else:
                minutes += dig
                if minutes > 59:
                    return None


        minute_string = str(minutes).zfill(2)
        return f"{hours}:{minute_string}"
    
arr = [
    1,
    9,
]
foo = arr[-1]
sol = Solution()
res = sol.readBinaryWatch(foo)
print(res)