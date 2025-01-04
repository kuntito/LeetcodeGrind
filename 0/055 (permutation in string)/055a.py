# https://leetcode.com/problems/permutation-in-string/description/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_map = {}
        for ch in s1:
            char_map[ch] = char_map.get(ch, 0) + 1

        for idx, ch in enumerate(s2):
            if ch in char_map:
                if self.explore(idx, s1, s2, char_map):
                    return True
                
        return False
    
    def explore(self, start_idx, s1, s2, char_map):
        perm_end = start_idx + len(s1)
        if perm_end > len(s2):
            return False
        
        map2 = {}
        for idx in range(start_idx, perm_end):
            ch = s2[idx]
            map2[ch] = map2.get(ch, 0) + 1

            if ch not in char_map or map2[ch] > char_map[ch]:
                return False
            
        return True
            

        


    
arr = [
    ["adc", "dcda"],
    ["ab", "eidboaoo"],
    ["ab", "eidbaooo"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.checkInclusion(foo, bar)
print(res)
