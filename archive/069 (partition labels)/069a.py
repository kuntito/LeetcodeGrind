# https://leetcode.com/problems/partition-labels/description/

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        char_map = {}

        for ch in s:
            char_map[ch] = char_map.get(ch, 0) + 1

        res = []
        streak = 0

        seen = {}
        for idx in range(len(s)):
            streak += 1
            ch = s[idx]
            seen[ch] = seen.get(ch, 0) + 1

            if seen[ch] == char_map[ch]:
                del seen[ch] 

            if not seen:
                res.append(streak)
                streak = 0

        return res
    

arr = [
    "xyxxyzbzbbisl",
    "abcabc",
    "ababcbacadefegdehijhklij",
    "eccbbbbdec",
]
foo = arr[-1]
sol = Solution()
res = sol.partitionLabels(foo)
print(res)

            