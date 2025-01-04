# https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
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
            count = self.counter[n]
            if not count: continue

            self.counter[n] -= 1
            arr.append(n)
            self.explore(arr)
            arr.pop()
            self.counter[n] += 1
                


arr = [
    [1,2],
    [1,1,3,3,3,2,1],
    [2,2, 1, 1, 1],
    [2,2, 1,],
    [2,2, 1, 1],
    [3,3,0,3],
]
foo = arr[-1]
sol = Solution()
res = sol.permuteUnique(foo)

for row in res:
    print(row)
