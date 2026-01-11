# https://leetcode.com/problems/shortest-word-distance-ii/description/


from collections import defaultdict


class WordDistance:
    def __init__(self, wordsDict: list[str]):
        self.wordMap = defaultdict(list)
        for idx, w in enumerate(wordsDict):
            self.wordMap[w].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        lsOne, lsTwo = self.wordMap[word1], self.wordMap[word2]

        smallest = float("inf")
        
        # let's apply a two pointer approach here where we always move the smaller index
        uno, dos = 0, 0
        while uno < len(lsOne) and dos < len(lsTwo):
            valOne, valTwo = lsOne[uno], lsTwo[dos]
            
            smallest = min(abs(valOne - valTwo), smallest)
            
            if valOne < valTwo:
                uno += 1
            else:
                dos += 1
                

        return smallest


arr = [
    ["practice", "makes", "perfect", "coding", "makes"],
]
foo = arr[-1]
sol = WordDistance(foo)

words = [
    ["makes", "coding"],
    ["coding", "practice"],
]
uno, dos = words[-1]
res = sol.shortest(uno, dos)
print(res)
