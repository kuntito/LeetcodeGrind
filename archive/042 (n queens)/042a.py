# https://leetcode.com/problems/n-queens/description/

# TODO https://www.youtube.com/watch?v=Ph95IHmRp5M
# 12:31
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        self.n = n
        self.res = []
        slots = [[0] * n for _ in range(n)]

        # for row in slots:
        #     print(row)

        self.explore(0, slots)
        return self.res

    def explore(self, ri, slots):
        if ri == len(slots):
            self.save(slots)
            return
        
        for ci in range(len(slots)):
            if slots[ri][ci] == 0:
                slots[ri][ci] = 'Q'
                self.foo(ri, ci, slots, increment=True)
                self.explore(ri + 1, slots)
                self.foo(ri, ci, slots, increment=False)
                slots[ri][ci] = 0


    def foo(self, r, c, slots, increment):
        for ri in range(r-1, r+2):
            for ci in range(c-1, c+2):
                if ri == r and ci == c:
                    continue
                inc_r = ri - r
                inc_c = ci - c
                self.exclude_reach(ri, ci, inc_r, inc_c, slots, increment)


    def exclude_reach(self, ri, ci, inc_ri, inc_ci, slots, increment):
        dim = len(slots)
        while ri >= 0 and ri < dim and ci >= 0 and ci < dim:
            if increment:
                slots[ri][ci] += 1
            else:
                slots[ri][ci] -= 1

            ri += inc_ri
            ci += inc_ci


    def save(self, slots):
        arr = []
        for row in slots:
            arr.append(
                ''.join([val if val == 'Q' else '.' for val in row])
            )
        
        self.res.append(arr)


arr = [
    3,
    4,
]
foo = arr[-1]
sol = Solution()


res = sol.solveNQueens(foo)
print(res)