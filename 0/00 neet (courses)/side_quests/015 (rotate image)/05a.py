# https://leetcode.com/problems/rotate-image/description/

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        if len(matrix) == 1: return
        rows, cols = len(matrix), len(matrix[0])
        
        first_ri, first_ci = 0, 0
        last_ri, last_ci = rows - 1, cols - 1
        while first_ri < last_ri:
            for _ in range(last_ci - first_ci):
                self.perform_rotation(
                    first_ri,
                    first_ci,
                    last_ri,
                    last_ci,
                    matrix,
                )

            first_ri += 1
            first_ci += 1

            last_ri -= 1
            last_ci -= 1


    def perform_rotation(
        self,
        first_ri,
        first_ci,
        last_ri,
        last_ci,
        matrix,
    ):
        directions = self.get_direction_arr(first_ri, first_ci, last_ri, last_ci)

        ri, ci = first_ri+1, first_ci
        prev = matrix[ri][ci]
        for increment, final_destination in directions:
            while (ri, ci) != final_destination:

                ri += increment[0]
                ci += increment[1]

                temp = matrix[ri][ci]
                matrix[ri][ci] = prev
                prev = temp



    def get_direction_arr(self, first_ri, first_ci, last_ri, last_ci):
        return [
            [(-1, 0), (first_ri, first_ci)],
            [(0, 1), (first_ri, last_ci)],
            [(1, 0), (last_ri, last_ci)],
            [(0, -1), (last_ri, first_ci)],
            [(-1, 0), (first_ri + 1, first_ci)],
        ]


arr = [
    [
        [1, 2],
        [3, 4],
    ],
    [
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16],
    ],
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
]
foo = arr[-1]

sol = Solution()
sol.rotate(foo)


for row in foo:
    print(row)