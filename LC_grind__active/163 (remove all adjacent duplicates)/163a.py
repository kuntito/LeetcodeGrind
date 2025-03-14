# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

# TODO link with `161. decode string`
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        pass
        # hashmap where you store (ch => lst)
        # the list contains the indices of the occurence of the chars
        # once you count `k` of each char
        # check if the elements in the list are consecutive
        # if they are create a tuple (start, end) of the consecutive range and store in a `set`
        
        # a list is consecutive if it contains i, i+1, i+2...
        # or [i, j, k..], where (i+1, j-1) is in the set
        
        char_map = {}
        seen = set()
        
        for idx, ch in enumerate(s):
            if ch not in char_map:
                char_map[ch] = []
                
            char_map[ch].append(idx)
            arr = char_map[ch]
            
            if len(arr) >= k:
                if self.is_consecutive(arr, seen):
                    ch_range = (arr[0], arr[-1])
                    seen.add(ch_range)
                    for _ in range(k):
                        char_map[ch].pop()
                    
        res = []
        for arr in char_map.values():
            for idx in arr:
                res.append(idx)
        res.sort()
        
        return ''.join([s[idx] for idx in res])
                
    def is_consecutive(self, arr, seen):
        
        for idx, chIdx in enumerate(arr):
            if idx == 0: continue
            # if it's not the direct previous
            # get the range and confirm it's been excluded
            prevChIdx = arr[idx - 1]
            if prevChIdx != chIdx - 1:
                pass
                ch_range = (prevChIdx + 1, chIdx-1)
                if ch_range not in seen:
                    return False
            
        return True
    
arr = [
    ["deeedbbcccbdaa", 3],
    ["pbbcggttciiippooaais", 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.removeDuplicates(foo, bar)
print(res)