# write the single row implementation
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        prev_row = [0 for _ in range(cols)]

        for ri in range(rows-1, -1, -1):
            cur_row = [0 for _ in range(cols)]
            for ci in range(cols-1, -1, -1):
                if text1[ri] == text2[ci]:
                    temp = 1
                    if ci + 1 < cols:
                        temp += prev_row[ci+1]
                    cur_row[ci] = temp
                else:
                    cur_row[ci] = prev_row[ci]
                    if ci + 1 < cols:
                        cur_row[ci] = max(cur_row[ci], cur_row[ci+1])
            prev_row = cur_row

        return prev_row[0]
    

items = [
    ["", ""],
    ["upr", "urp"],
    ["pqrs", "sqrp"],
    ["ab", "abc"],
    ["bbm", "mb"],
    ["hcbgcrcbh", "ghbrgc"],
    ["abcde", "ace"],
    ["bsbininm", "jmjkbkjkv"],
    ["ace", "ace"],
    ["abcba", "abcbcba"],
]

foo = items[-1]


uno, dos = items[-1]
sol = Solution()
res = sol.longestCommonSubsequence(uno, dos)
print(res)