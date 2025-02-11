# https://leetcode.com/problems/extra-characters-in-a-string/description/

class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        pass
    
        
        words = set(dictionary)
        # final answer should be len(s) - self.explore(...)
        self.explore(s, words, 0)

    def explore(self, chars, dik, curLen):
        pass
        # iterate through `chars` with index
        # for each index, find out if any words end at that index
        # for all the words that end there
        # start a recursive loop (chars[idx+1: ], words, curWordLen)
        # return the maxWordLen
        
        tmpLen = 0
        dim = len(chars)
        for idx in range(dim):
            words_here = self.get_words_end_here(idx, chars, dik)
            for w in words_here:
                print(w)
                # w_len = len(w)
                # foo = self.explore(
                #     chars[idx + 1:], dik, w_len
                # )
            
                # tmpLen = max(
                #     tmpLen,
                #     foo,
                # )
                
        return curLen + tmpLen
    
    
    def get_words_end_here(self, end_idx, chars, dik):
        pass
        res = []
        for w in dik:
            if len(w) - 1 > end_idx:
                continue
            
            # TODO wrong condition
            # the word has to end at `end_idx`
            # get the start_idx relative to `end_idx`
            # only append if they match
            if w in chars[:end_idx]:
                res.append(w)
                
        return res
        
arr = [
    ["leetscode", ["leet","code","leetcode"]],
]
foo, bar = arr[-1]
sol = Solution()
sol.minExtraChar(foo, bar)
