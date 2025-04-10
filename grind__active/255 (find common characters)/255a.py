# https://leetcode.com/problems/find-common-characters/

from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        counter = Counter(words[0])

        for w in words[1:]:
            counter &= Counter(w)

        res = []
        for ch, count in counter.items():
            for _ in range(count):
                res.append(ch)
        return res