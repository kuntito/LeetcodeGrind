from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonCounter = Counter("balloon")

        textCounter = Counter()
        for ch in text:
            if ch in balloonCounter:
                textCounter[ch] = textCounter.get(ch, 0) + 1

        count = 0
        while textCounter:
            for ch in balloonCounter:
                if ch not in textCounter:
                    return count

                textCounter[ch] -= balloonCounter[ch]
                if textCounter[ch] < 0:
                    return count
                if textCounter[ch] == 0:
                    del textCounter[ch]

            count += 1

        return count