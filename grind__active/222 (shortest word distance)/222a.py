class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        # go through the array
        # the idea is to track the distances for any pair found
        # use a variable, `tmp` to indicate the first word in the pair

        # `tmp` is initialized to None
        # on finding the first word, update the value of `tmp`

        minDist = len(wordsDict)
        targets = (word1, word2)
        tmp = None
        for idx, word in enumerate(wordsDict):
            if word in targets:
                # if it's a different word
                # calculate the distance
                if tmp is not None and tmp[0] != word:
                    dist = idx - tmp[1]
                    minDist = min(
                        minDist,
                        dist
                    )
                tmp = (word, idx)

        return minDist
        
arr = [
    [["a","b","c","d","d"], "a", "d"]
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.shortestDistance(foo, bar, baz)
print(res)