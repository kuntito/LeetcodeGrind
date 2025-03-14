# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.res = []
        self.counter = {}
        self.nums = nums

        for n in self.nums:
            self.counter[n] = self.counter.get(n, 0) + 1

        self.explore([])

        return self.res
    
    def explore(self, arr):
        if len(arr) == len(self.nums):
            self.res.append(arr[::])
            return
        for n in self.counter:
            if not self.counter[n]:
                continue
            arr.append(n)
            self.counter[n] -= 1
            self.explore(arr)
            self.counter[n] += 1
            arr.pop()


arr = [
    [1, 2],
]

foo = arr[-1]
sol = Solution()
res = sol.permute(foo)
print(res)