class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set()
        for n in nums:
            seen.add(n)

        res = 0
        for n in nums:
            if n-1 not in seen:
                foo = n
                while foo + 1 in seen:
                    foo += 1
                res = max(
                    res,
                    (foo - n) + 1,
                )
                
        return res