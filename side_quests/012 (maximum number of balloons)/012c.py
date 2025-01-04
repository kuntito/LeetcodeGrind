from collections import Counter

# TODO https://neetcode.io/solutions/maximum-number-of-balloons
# 02:20
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonCounter = Counter("balloon")

        textCounter = Counter()
        for ch in text:
            if ch in balloonCounter:
                textCounter[ch] = textCounter.get(ch, 0) + 1

        lowest = len(text)
        for ch in balloonCounter:
            count = textCounter.get(ch, 0) // balloonCounter.get(ch)
            lowest = min(lowest, count)
            if lowest == 0:
                return 0
            
        return lowest
    
arr = [
    "nlaebolko",
    "balon",
    "loonbalxballpoon",
]
foo = arr[-1]
sol = Solution()
res = sol.maxNumberOfBalloons(foo)
print(res)
            