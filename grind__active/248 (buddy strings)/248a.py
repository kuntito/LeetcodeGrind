# https://leetcode.com/problems/buddy-strings/

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        pass
        # what does it mean to swap two letters and have it equal to another
        # our answer string would have EXACTLY two letters out of place
        # such that when those two letters are swapped, they equal `goal`
        
        # for edge cases, if the number of misplaced letters do NOT equal `2`
        # return False
        # use a list to track the out of place letters plus their indices, `arr`
        # if the len(arr) becomes > 2: return False
        
        # another edge case, if `s` and `goal` are different sizes, return False
        
        # if after iteration, len(arr) < 2: return False
        # find the indices for the out of place letters, `i`, `j`
        
        # check if when swapped, they equal `goal`
        # a short hand for this is `goal[i] == s[j]`
        # `goal[j] == s[i]`
        
        if len(s) != len(goal): return False
        
        dim = len(s)
        arr = []
        for idx in range(dim):
            chOne, chTwo = s[idx], goal[idx]
            
            if chOne != chTwo:
                arr.append((chOne, chTwo))
                
            if len(arr) > 2:
                return False
            
        if len(arr) != 2:
            # for 'aa' and 'aa'
            # they can be swapped, your current algo would return an empty list
            # which would be a false negative
            
            # how do you account for the swappable indices having the same chars
            # this is a special case and when it happens `len(arr) == 0`
            
            # at this point, it's guaranteed the strings are equal lengths
            # and have the same char configuration, we just need to know if
            # either one has two of the same characters
            if len(arr) == 0:
                counter = {}
                for ch in s:
                    counter[ch] = counter.get(ch, 0) + 1
                    if counter[ch] == 2:
                        return True
                
            return False
        
        
        uno, dos = arr
        
        return uno[0] == dos[1] and uno[1] == dos[0]
    
arr = [
    ["ab", "ba"],
    ["ab", "ab"],
    ["aa", "aa"], # this should return `True`
]
foo, bar = arr[-1]
sol = Solution()
res = sol.buddyStrings(foo, bar)
print(res)
        
        