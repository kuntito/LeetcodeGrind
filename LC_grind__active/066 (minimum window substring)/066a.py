# https://leetcode.com/problems/minimum-window-substring/description/

# TODO https://neetcode.io/solutions/minimum-window-substring
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        self.res = ""

        teeCounter = Counter(t)
        essCounter = Counter()

        self.explore(s, teeCounter, essCounter)
        
        return s[self.res[0]:self.res[1]] if self.res else self.res
    
    def explore(self, s, teeCounter, essCounter):
        leftIdx = 0
        dim = len(s)
        while leftIdx < dim and s[leftIdx] not in teeCounter:
            leftIdx += 1

        # loop through `s` with idx, 
        for idx in range(leftIdx, dim):
            ch = s[idx]
            # keep going, updating  essCounter
            essCounter[ch] = essCounter.get(ch, 0) + 1

            # when (essCounter & teeCounter) == teeCounter
            if (essCounter & teeCounter) == teeCounter:
                # update `self.res` with a shorter valid window
                rightIdx = idx + 1
                if not self.res:
                    self.res = (leftIdx, rightIdx)
                else:
                    currLen = (idx - leftIdx) + 1

                    left, right = self.res
                    resLen = (right - left)
                    if currLen < resLen:
                        self.res = (leftIdx, rightIdx)

                # remove the char and leftIdx, possibly invalidating the window
                ch = s[leftIdx]
                essCounter[ch] -= 1
                leftIdx += 1

                # move `leftIdx` forward until
                # it reaches the first `ch` in `teeCounter` that doesn't make up
                # a valid window
                # if none, it should move past `idx`
                while leftIdx <= idx:
                    ch = s[leftIdx]

                    if (essCounter & teeCounter) == teeCounter:
                        # update `self.res` with a shorter valid window
                        rightIdx = idx + 1
                        currLen = (idx - leftIdx) + 1

                        left, right = self.res
                        resLen = (right - left)
                        if currLen < resLen:
                            self.res = (leftIdx, rightIdx)
                    elif ch in teeCounter:
                        break

                    essCounter[ch] -= 1
                    leftIdx += 1

    
arr = [
    ["ADOBECODEBANC", "A"],
    ["a", "b"],
    ["bba", "ab"],
    ["ADOBECODEBANC", "ABC"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minWindow(foo, bar)
print(res)