# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        pass
    
        # define a recursive function that takes 
        # (index, p_map, and s)
        # for each recursive function
        # call another one (index+1, p_map and s)
        
        # create a temp_map = {}
        # start iterating from index
        # append each char to the map
        # if temp_map[ch] > p_map[ch]
        # return None
        
        p_map = Counter(p)
        
        res = []
        dim = len(s)
        for idx in range(dim):
            foo = self.explore(idx, p, p_map, s)
            if foo is not None:
                res.append(foo)
        
        return res
    
    def explore(self, start_idx, p, p_map, s):
        pass

        have, need = 0, len(p_map)
    
        dim = len(s)
        temp = {}
        
        lim = min(start_idx + len(p), dim)
        for idx in range(start_idx, lim):
            ch = s[idx]
            if ch not in p_map:
                return None
            
            temp[ch] = temp.get(ch, 0) + 1
            if temp[ch] > p_map[ch]:
                return None

            if temp[ch] == p_map[ch]:
                have += 1
            
        return start_idx if have == need else None
    

arr = [
    ["cbaebabacd", "abc"],
    ["abab", "ab"],
    ["baa", "aa"]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findAnagrams(foo, bar)
print(res)
            
            