# https://leetcode.com/problems/longest-string-chain/description/

from collections import defaultdict


class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        pass
        # it's giving dp
        # we want to find the longest chain. 
        # what's a chain? an array of words where each word differs from the next by one character
        # and the relative order between the words are the same
        
        # for instance, ca => cat
        # both words differ by one character
        # in both words 'c' precedes 'a'

        # another example is ct => cat
        # both words differ by one character
        # and in both 'c' precedes 't'
        
        # tc => cat would be False, even though they differ by one character
        # 't' doesn't precede 'c' in 'cat'
        
        # that said, we can move from low to high
        # find words with the least length,
        
        # consider `["a", "b", "ba", "bca", "bda", "bdca"]`, the least length is `1`
        # for each word in that group, see if it can connect to words with `2` characters
        # for each `2` char word, see if there's a three, repeat until you run out of words
        # and store track the longest chain
        
        # the function would benefit from grouping words based on length
        # and memoizing the chain search for each word, since it's bound to be the same each time
        
        # first, buckets
        buckets = defaultdict(list)
        
        
        for w in words:
            dim = len(w)
            buckets[dim].append(w)
            
        
        words.sort()
        # we'd go through each word and explore it's longest chain
        
        longestChain = 0
        memo = {}
        for w in words:
            longestChain = max(
                longestChain,
                self.explore(w, buckets, memo)
            )
        return longestChain
            
    def explore(self, word, buckets, memo):
        if word in memo:
            return memo[word]
        
        longest = 0
        
        nextBucket = len(word) + 1
        for nextWord in buckets[nextBucket]:
            if not self.ifOrderSame(word, nextWord): continue
            fooLen = self.explore(nextWord, buckets, memo)
            longest = max(
                longest,
                fooLen
            )
            
        memo[word] = longest + 1
        return memo[word]
    
    def ifOrderSame(self, wordOne, wordTwo):
        pass
        # the omitted character could be anywhere
        # at the start, inbetween or end
        
        # if at the start what would this mean
        # wordOne == wordTwo[1:]
        
        # if in between, what would this mean
        # it would mean, wordOne and wordTwo would have the same characters
        # up to a point where wordOne doesn't have said character
        # at that point, we'd fashi, but we can only fashi once
        
        # if we fashi again, that's two chars
        
        
        # what about the end?
        # i think the fashi argument works for both
        
        # two indices
        uno, dos = 0, 0
        
        count = 0
        while dos < len(wordTwo):
            chOne = wordOne[uno] if uno < len(wordOne) else "."
            chTwo = wordTwo[dos]
            
            if chOne == chTwo:
                uno += 1
            else:
                # at this point, they differ, i assume this is the differing character
                # i.e. `at => cat`
                # i.e. `ct => cat`
                # i.e. `ca => cat`
                count += 1

            if count > 1:
                return False
                            
            dos += 1
        
        return count == 1



arr = [
    ["a", "b", "ba", "bca", "bda", "bdca"],
    ["a","b","ab","bac"],
    ["xbc","pcxbcf","xb","cxbc","pcxbc"],
    ["qyssedya","pabouk","mjwdrbqwp","vylodpmwp","nfyqeowa","pu","paboukc","qssedya","lopmw","nfyqowa","vlodpmw","mwdrqwp","opmw","qsda","neo","qyssedhyac","pmw","lodpmw","mjwdrqwp","eo","nfqwa","pabuk","nfyqwa","qssdya","qsdya","qyssedhya","pabu","nqwa","pabqoukc","pbu","mw","vlodpmwp","x","xr"],
]
foo = arr[-1]
sol = Solution()
res = sol.longestStrChain(foo)
# res = sol.ifOrderSame("tc", "cat")
print(res)
