# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        seen = set()

        for n in nums:
            sub = [n]
            seen.add(n)
            self.explore_permute(n, sub, res, seen, nums)
            sub.pop()
            seen.remove(n)

        return res
    
    def explore_permute(self, start, sub: list, res: list, seen: set, nums: list):
        for n in nums:
            if n in seen: continue

            sub.append(n)
            seen.add(n)
            self.explore_permute(n, sub, res, seen, nums)
            sub.pop()
            seen.remove(n)
        
        if len(sub) == len(nums):
            res.append(sub.copy())


arr = [
    [1, 2],
]

foo = arr[-1]
sol = Solution()
res = sol.permute(foo)
print(res)