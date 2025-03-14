# https://leetcode.com/problems/combination-sum-ii/description/


# TODO https://www.youtube.com/watch?v=FOyRpNUSFeA
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        self.candidates = candidates
        self.candidates.sort()

        self.res = []
        self.explore(0, target, [])

        return self.res
    
    def explore(self, start_idx, target, stack):
        if target == 0:
            self.res.append(stack[::])
            return

        idx = start_idx
        while idx < len(self.candidates):
            n = self.candidates[idx]
            if n > target:
                break
            stack.append(n)
            self.explore(
                idx + 1,
                target-n,
                stack,
            )
            stack.pop()

            while idx + 1 < len(self.candidates) and self.candidates[idx + 1] == n:
                idx += 1
            idx += 1


arr = [
    [[10,1,2,7,6,1,1,5], 8],
]
foo, bar = arr[-1]
print(sorted(foo))
sol = Solution()
res = sol.combinationSum2(foo, bar)
print(res)