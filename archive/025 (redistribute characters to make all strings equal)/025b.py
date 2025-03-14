# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        # can the freq of each character be evenly divided 
        # by the number of items in the `words`
        pass
    
        counter = {}
        for w in words:
            for ch in w:
                counter[ch] = counter.get(ch, 0) + 1
                
        dim = len(words)
        for ch, count in counter.items():
            if count % dim:
                return False
            
        return True
    
    
arr = [
    ['a', 'b'],
    ["abc","aabc","bc"],
    ["aaaab","b"],
    ["ab","a"],
]
foo = arr[-1]
sol = Solution()
res = sol.makeEqual(foo)
print(res)