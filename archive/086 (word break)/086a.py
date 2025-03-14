# https://leetcode.com/problems/word-break/description/


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        pass
        # turn `wordDict` to a set
        wordDict = set(wordDict)
        # define a recursive function explore(idx, s, wordDict)
        # `idx` is the starting position of the iteration
        
        # create a variable `curr`, that tracks every character, `ch`, in the iteration
        # for every character found, concatenate it with `curr`
        # check if `curr in wordDict`, if yes,
        # start another recursive call with `explore(idx + 1, s, wordDict)`
        # if `idx + 1 == len(s): return True`
        
        return self.explore(0, s, wordDict, {})
    
    def explore(self, startIdx, chars, wordDict, memo):
        if startIdx in memo:
            return memo[startIdx]
        
        dim = len(chars)
        if startIdx == dim:
            return True

        curr = ""
        for idx in range(startIdx, dim):
            ch = chars[idx]
            curr += ch
            
            if curr in wordDict:
                if self.explore(idx + 1, chars, wordDict, memo):
                    memo[startIdx] = True
                    return memo[startIdx]
                
        memo[startIdx] = False
        return memo[startIdx]


arr = [
    ["catsandog", ["cats","dog","sand","and","cat"]],
    ["leetcode", ["leet","code"]],
    ["applepenapple", ["apple","pen"]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.wordBreak(foo, bar)
print(res)