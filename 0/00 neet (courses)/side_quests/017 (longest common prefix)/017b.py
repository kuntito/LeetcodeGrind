# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
                
            res += strs[0][i]

        return res
    
arr = [
    ["dog","racecar","car"],
    ["flower","flow","flight"],
]
foo = arr[-1]
sol = Solution()
res = sol.longestCommonPrefix(foo)

print(res)