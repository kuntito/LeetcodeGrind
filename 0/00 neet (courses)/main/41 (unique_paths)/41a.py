# https://leetcode.com/problems/unique-paths/description

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [0 for _ in range(n)]

        for _ in range(m - 1, -1, -1):
            cur_row = [0 for _ in range(n)]
            cur_row[-1] = 1
            for ci in range(n - 2, -1, -1):
                cur_row[ci] = prev_row[ci] + cur_row[ci+1]
            prev_row = cur_row


        return prev_row[0]