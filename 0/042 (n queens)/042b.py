# https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        self.dim = n
        self.cols = set()
        self.pos_diag = set()
        self.neg_diag = set()
        self.res = []

        slots = [['.' for _ in range(n)] for _ in range(n)]
        self.explore(0, slots)
        return self.res
    
    def explore(self, ri, slots):
        if ri == self.dim:
            self.save(slots)

        for ci in range(self.dim):
            pos_diag = ri - ci
            neg_diag = ri + ci
            if ci in self.cols or pos_diag in self.pos_diag or neg_diag in self.neg_diag:
                continue
            slots[ri][ci] = 'Q'
            self.cols.add(ci)
            self.pos_diag.add(pos_diag)
            self.neg_diag.add(neg_diag)
            self.explore(ri + 1, slots)
            self.cols.remove(ci)
            self.pos_diag.remove(pos_diag)
            self.neg_diag.remove(neg_diag)
            slots[ri][ci] = '.'


    def save(self, slots):
        arr = [''.join(row) for row in slots]
        self.res.append(arr)


arr = [
    3,
    4,
]
foo = arr[-1]
sol = Solution()


res = sol.solveNQueens(foo)
print(res)