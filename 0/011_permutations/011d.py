class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = [[]]

        for n in nums:
            temp = []
            for p in res:
                for idx in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(idx, n)
                    temp.append(p_copy)
            res = temp

        return res


arr = [
    [1, 2],
]

foo = arr[-1]
sol = Solution()
res = sol.permute(foo)
print(res)