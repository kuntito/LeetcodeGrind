# https://leetcode.com/problems/word-break-ii/

# TODO https://neetcode.io/solutions/word-break-ii
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        pass
        # reverse iterate through `s` with index
        # use a hashmap to determine what dictionary words that be formed at that index
        # do this for all indices
        
        # recursively explore from index `0`
        # run a loop through all the words that can be formed from index `0`
        # determine the end of the word `0 + len(word)`
        # start another recursive call
        # if you hit idx == dim
        # it means you've found a valid word break
        # concatenate with a space and append to `self.res`
        
        self.wordsAtIdx = self.get_words_at_index(s, wordDict)

        self.dim = len(s)
        self.space = " "
        self.res = []
        self.explore(0, [])
        
        return self.res
    
    def explore(self, idx, arr):
        if idx == self.dim:
            self.res.append(self.space.join(arr))
            return
        
        for w in self.wordsAtIdx[idx]:
            arr.append(w)
            self.explore(
                idx + len(w),
                arr,
            )
            arr.pop()
        
        
    def get_words_at_index(self, chars, words):
        pass
        # with index, reverse iterate through chars
        # at each index, check if any word can start there
        
        wordsAtIdx = defaultdict(list)
        
        dim = len(chars)
        for idx in range(dim-1, -1, -1):
            slice = chars[idx:]
            for w in words:
                if slice.startswith(w):
                    wordsAtIdx[idx].append(w)
                
        return wordsAtIdx

arr = [
    ["catsanddog", ["cat","cats","and","sand","dog"]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.wordBreak(foo, bar)
for i in res:
    print(i)