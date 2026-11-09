from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        targetDict = self.makeDict(p)
        window = defaultdict(int)

        res = []

        idx = 0
        winStartIdx = None
        
        dim = len(s)
        while idx < dim:
            ch = s[idx]

            if ch in targetDict:
                window[ch] += 1
                if winStartIdx is None:
                    winStartIdx = idx

                while window[ch] > targetDict[ch]:
                    chAtWinStart = s[winStartIdx]
                    
                    window[chAtWinStart] -= 1
                    
                    winStartIdx += 1

                if window == targetDict:
                    res.append(winStartIdx)
            else:
                window.clear()
                winStartIdx = None

            idx += 1

        return res



    def makeDict(self, s):
        counter = {}

        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1

        return counter


arr = [
    ["cbaebabacd", "abc"],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.findAnagrams(foo, bar)
print(res)