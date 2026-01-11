# https://leetcode.com/problems/regular-expression-matching/description/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass
        # declare a pointer for the string
        # divide the pattern into parts
        
        patterns = self.get_pattern_units(p)
        
        dot = "."
        idxMain = 0
        dimMain = len(s)
        # for each pattern, match it in the main string
        for pat in patterns:
            pass
            if pat == dot:
                if idxMain == dimMain:
                    return False
                idxMain += 1
            elif pat.isalpha():
                if idxMain == dimMain:
                    return False
                if pat != s[idxMain]:
                    return False
                idxMain += 1
            else:
                pass
                ch, _ = pat
                while idxMain < dimMain and (ch == dot or ch == s[idxMain]):
                    idxMain += 1
            
            
        return idxMain == len(s)
        

    def get_pattern_units(self, chars):
        pass
        patterns = []

        ast = "*"
        dim = len(chars)
        idx = 0
        while idx < dim:
            ch = chars[idx]
            
            if idx + 1 < dim and chars[idx + 1] == ast:
                patterns.append(ch + ast)
                idx += 1
            else:
                patterns.append(ch)
            
            idx += 1
            
        return patterns


arr = [
    ["aab", "c*a*b"],
    ["aa", "a*"],
    ["ab", ".*"],
    ["aaa", "a*a"] # TODO, deep this edge case
]
foo, bar = arr[-1]
sol = Solution()
res = sol.isMatch(foo, bar)
print(res)
        