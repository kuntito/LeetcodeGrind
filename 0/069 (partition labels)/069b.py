# https://leetcode.com/problems/partition-labels/description/

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurred = {}
        for idx in range(len(s) - 1, -1, -1):
            ch = s[idx]
            if ch not in last_occurred:
                last_occurred[ch] = idx

        res = []
        start = 0
        end = last_occurred[s[0]]
        for idx, ch in enumerate(s):
            end = max(
                end,
                last_occurred[ch]
            )

            if idx == end:
                res.append(end - start + 1)
                start = idx + 1

        return res
    

arr = [
    "xyxxyzbzbbisl",
    "eccbbbbdec",
    "abcabc",
    "eaaaabaaec",
    "ababcbacadefegdehijhklij",
]
foo = arr[-1]
sol = Solution()
res = sol.partitionLabels(foo)
print(res)
