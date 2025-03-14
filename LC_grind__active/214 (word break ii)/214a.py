# https://leetcode.com/problems/word-break-ii/description/

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        pass
    
        # iterate through `s`, keep track of each character seen, `tmp`
        # if `tmp in dict`
        # start a recursive call at idx + 1
        # store the found word in `arr`
        allWords = set(wordDict)
        arr = []
        self.res = []
        
        self.explore(arr, s, allWords)
        
        for it in self.res:
            print(it)
        
    def explore(self, arr, chars, allWords):
        if not chars:
            self.res.append(arr[::])
            return
        
        tmp = ""
        for idx, ch in enumerate(chars):
            tmp += ch
            if tmp in allWords:
                arr.append(tmp)
                self.explore(arr, chars[idx + 1:], allWords)
                arr.pop()
    
arr = [
    ["catsanddog", ["cat","cats","and","sand","dog"]],
    ["pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.wordBreak(foo, bar)
