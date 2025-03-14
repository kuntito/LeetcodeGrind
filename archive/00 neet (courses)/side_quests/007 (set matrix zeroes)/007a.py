class Solution:
    def setZeroes(self, matrix: list):
        """
        Do not return anything, modify matrix in-place instead.
        """
        queue = set()

        rows, cols = len(matrix), len(matrix[0])
        for ri in range(rows):
            for ci in range(cols):
                if matrix[ri][ci] == 0:
                    queue.add((ri, ci))

        seen_rows = set()
        seen_cols = set()
        for pos in queue:
            self.apply_zeroes(pos, seen_rows, seen_cols, matrix)


    def apply_zeroes(self, pos, seen_rows, seen_cols, matrix):
        rows, cols = len(matrix), len(matrix[0])
        og_ri, og_ci = pos

        if og_ri not in seen_rows:
            seen_rows.add(og_ri)

            for ci in range(cols):
                matrix[og_ri][ci] = 0


        if og_ci not in seen_cols:
            seen_cols.add(og_ci)

            for ri in range(rows):
                matrix[ri][og_ci] = 0   



arr = [
    [[1,1,1],[1,0,1],[1,1,1]],
    [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
]
foo = arr[-1]
sol = Solution()

sol.setZeroes(foo)

for row in foo:
    print(row)