# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        temp = strs[0]
        length = len(strs[0])

        for s in strs[1:]:
            temp_end = -1
            for i in range(min(len(s), length)):
                ch_one, ch_two = temp[i], s[i]
                if ch_one != ch_two:
                    break

                temp_end = i
            length = temp_end + 1
            if length == 0:
                break

        return temp[:length]
    

arr = [
    ["dog","racecar","car"],
    ["flower","flow","flight"],
]
foo = arr[-1]
sol = Solution()
res = sol.longestCommonPrefix(foo)

print(res)
