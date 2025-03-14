# https://leetcode.com/problems/maximum-number-of-balloons/description/
from collections import Counter

# https://neetcode.io/solutions/maximum-number-of-balloons
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonCounter = Counter("balloon")

        textCounter = Counter()
        for ch in text:
            if ch in balloonCounter:
                textCounter[ch] = textCounter.get(ch, 0) + 1

        lowestMultiple = float("inf")
        for ch in balloonCounter:
            if ch in textCounter:
                pass
                count = textCounter[ch]
                # ratio?
                multiple = count // balloonCounter[ch]
                lowestMultiple = min(lowestMultiple, multiple)
            else:
                return 0
            
        return lowestMultiple
    
arr = [
    "nlaebolko",
    "balon",
    "loonbalxballpoon",
]
foo = arr[-1]
sol = Solution()
res = sol.maxNumberOfBalloons(foo)
print(res)
            