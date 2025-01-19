# https://leetcode.com/problems/regular-expression-matching/description/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass
        # declare a pointer for the string
        
        idxMain = 0
        dimMain = len(s)
        
        prev_chars = []
        period, asterisk = '.', '*'
        
        for ch in p:
            if ch == period:
                prev_chars.append(ch)
                idxMain += 1
            elif ch == asterisk:
                if not prev_chars:
                    return False
                
                prevCh = prev_chars[-1]
                
                # you need at least one iteration for it to be valid
                # `idxMain` must have values in the tank, else return False
                if idxMain == dimMain:
                    return False
                
                # move forward while the char at idxMain is equal to prevCh
                while idxMain < dimMain and (prevCh == period or s[idxMain] == prevCh):
                    idxMain += 1
            else:
                if ch != s[idxMain]:
                    return False
                prev_chars.append(ch)
            
            
        return idxMain == dimMain
    
arr = [
    ["aa", "a*"],
    ["ab", ".*"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.isMatch(foo, bar)
print(res)
        