# https://leetcode.com/problems/combinations/description/

class Solution:
    def combine(self, n: int, k: int) -> list:
        self.combs = []
        self.n = n
        self.k = k

        self.explore(1, [])

        return self.combs
        
    def explore(self, start_num, sublist):
        if len(sublist) == self.k:
            self.combs.append(sublist[::])

        if start_num > self.n:
            return
        
        for num in range(start_num, self.n + 1):
            sublist.append(num)
            self.explore(num + 1, sublist)
            sublist.pop()


arr = [
    [4, 2],
    [4, 3],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.combine(foo, bar)
print(res)