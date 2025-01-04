# https://leetcode.com/problems/verifying-an-alien-dictionary/description/

# TODO https://neetcode.io/solutions/verifying-an-alien-dictionary
class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        pass
        order_map = {}
        for idx, ch in enumerate(order):
            order_map[ch] = idx
        
        dim = len(words)
        for idx in range(1, dim):
            wordOne, wordTwo = words[idx-1], words[idx]
            if not self.is_lexi_sort(wordOne, wordTwo, order_map):
                return False
        
        
        return True
    
    def is_lexi_sort(self, one, two, order_map):
        pass
        # to determine if two words are lexicographically sorted,
        # determine the first differing characters between those words
        # if the left char postion <= right char postion
        # the two words are sorted
        # else they aren't lexi sorted
        
 
        oneIdx, twoIdx = 0, 0
        while oneIdx < len(one) and twoIdx < len(two):
            chOne = one[oneIdx]
            chTwo = two[twoIdx]
            if chOne != chTwo:
                if order_map[chOne] > order_map[chTwo]: return False
                break
            
            oneIdx += 1
            twoIdx += 1
        
        # also, if you run out of matching characters in the right word
        # while the left word still has characters
        # the words aren't lexi sorted
        # i.e. "apple" and "app"
        # the correct order should be "app" and "apple"
        if twoIdx == len(two) and oneIdx < len(one):
            return False
        
        return True
    
arr = [
    [["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"],
    [["word","world","row"], "worldabcefghijkmnpqstuvxyz"],
    [["apple","app"], "abcdefghijklmnopqrstuvwxyz"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.isAlienSorted(foo, bar)
print(res)