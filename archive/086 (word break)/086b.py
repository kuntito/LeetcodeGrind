# https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        pass
        memo = { len(s): True }
    
        # iterate backwards through `s` using `idx`
        for idx in range(len(s)-1, -1, -1):
            pass
            # for every character, `idx`, check if any word in `wordDict` starts at `idx`
            # if yes, recurisvely check from the end of that word + 1
            
            # i.e if you check [2:5], and it's valid, check [5:?]
            # if all the checks are valid
            # memoize `idx`
            self.explore(idx, s, wordDict, memo)
            
        return memo[0]
        
    def explore(self, idx, startWord, words, memo):
        if idx in memo:
            return memo[idx]
        
        
        for w in words:
            end_range = idx + len(w)
            chars = startWord[idx: end_range]
            if end_range <= len(startWord) and chars == w:
                if self.explore(end_range, startWord, words, memo):
                    memo[idx] = True
                    return memo[idx]
                
                
        memo[idx] = False
        return memo[idx]
                


arr = [
    ["catsandog", ["cats","dog","sand","and","cat"]],
    ["leetcode", ["leet","code"]],
    ["applepenapple", ["apple","pen"]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.wordBreak(foo, bar)
print(res)