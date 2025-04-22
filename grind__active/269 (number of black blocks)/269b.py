# https://leetcode.com/problems/number-of-black-blocks/description/


# TODO can i target the black cells individually?
# probably, how about the zero cells
# i think i can math my way into the number of blocks
# the zero blocks would be the count of all the blocks minus the black cell blocks

# TODO, is my intuition wrong.
# doing top left and top right
class Solution:
    def countBlackBlocks(
        self, m: int, n: int, coordinates: list[list[int]]
    ) -> list[int]:
        pass

        pool = set([(ri, ci) for ri, ci in coordinates])
        # print(pool)
        res = [0 for _ in range(5)]
        rows, cols = m, n
        # for each coordinate, check it's squares
        # bottom right,
        # bottom left
        # top right
        # top left
        for ri, ci in coordinates:

            # top right
            locs = (
                (ri, ci - 1),
                (ri, ci),
                (ri + 1, ci - 1),
                (ri + 1, ci),
            )
            sq_count = self.get_count(locs, rows, cols, pool)
            if sq_count:
                res[sq_count] += 1

            # top left
            locs = (
                (ri, ci),
                (ri, ci + 1),
                (ri + 1, ci),
                (ri + 1, ci + 1),
            )
            sq_count = self.get_count(locs, rows, cols, pool)
            if sq_count:
                res[sq_count] += 1

        total_blocks = (rows - 1) * (cols - 1)

        zero_count = total_blocks - sum(res)
        res[0] = zero_count

        return res

    def get_count(self, locs, rows, cols, pool):
        count = 0
        for ri, ci in locs:
            if ri < 0 or ri == rows or ci < 0 or ci == cols:
                return 0

            if (ri, ci) in pool:
                count += 1

        return count


arr = [
    [3, 3, [[0, 0]]],
    # [3, 3, [[0,0],[1,1],[0,2]]],
    [
        32,
        32,
        [
            [17, 29],
            [29, 16],
            [19, 20],
            [18, 9],
            [16, 7],
            [20, 25],
            [22, 19],
            [4, 9],
            [14, 17],
            [6, 23],
            [2, 2],
            [20, 1],
            [8, 7],
            [4, 7],
            [14, 14],
            [10, 10],
            [1, 27],
            [18, 23],
            [6, 30],
            [8, 18],
            [26, 23],
            [25, 8],
            [5, 6],
            [3, 4],
        ],
    ],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.countBlackBlocks(foo, bar, baz)
print(res)
