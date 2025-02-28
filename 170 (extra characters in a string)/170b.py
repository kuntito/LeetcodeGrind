# https://leetcode.com/problems/extra-characters-in-a-string/description/

class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        pass
        # convert dictionary into a set
        self.dictionary = set(dictionary)
        
        # iterate through `s` with index
        # at each index, find all the words that end at that index
        # if none exists, proceed
        
        # if they exist, start a recursive function with `s[idx + 1 : ]`
        # each recursive function should return the least amount of extra characters left
        return self.explore(s, {})
        
    def explore(self, chars, memo):
        if chars in memo:
            return memo[chars]
        
        minLen = len(chars)
        dim = len(chars)
        for idx in range(dim):
            pass
            words_here = self.find_words_that_end_here(idx, chars)
            for w in words_here:
                pass
                # to determine the extra characters
                # find the length of the string till idx,
                # which would be `idx + 1`, stringLen
                # do stringLen - len(word), as `tmp`
                # tmp += self.explore(s[idx + 1: ])
                # update minLen
                currLen = idx + 1
                extras = currLen - len(w)
                
                extras += self.explore(chars[idx+1:], memo)
                minLen = min(
                    minLen,
                    extras
                )
                
        memo[chars] = minLen
        return memo[chars]
        
    def find_words_that_end_here(self, end_idx, chars):
        pass
        res = []
        # iterate up till `idx`
        # check each slice if it exists in dictionary
        end_range = end_idx + 1
        for i in range(end_range):
            slice = chars[i: end_range]
            if slice in self.dictionary:
                res.append(slice)
                
        return res
                
        
arr = [
    ["leetscode", ["leet","code","leetcode"]],
    ["sayhelloworld", ["hello","world"]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minExtraChar(foo, bar)
print(res)
