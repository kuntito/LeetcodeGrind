# https://leetcode.com/problems/assign-cookies/description/

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()


        size_idx = 0
        greed_idx = 0

        while size_idx < len(s) and greed_idx < len(g):
            # starting with the first idx in `s`
            # get the size and move through each value in `g`
            greed = g[greed_idx]
            size = s[size_idx]
            # if `size` >= `greed`:
            # move greed idx forward
            if size >= greed:
                greed_idx += 1
            size_idx += 1
            # move size idx forward
            # if `size` < greed:
            # move `size idx` forward
        return greed_idx

    
arr = [
    [[1, 2], [1, 2, 3]],
    [[1, 2, 3], [1, 1]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findContentChildren(foo, bar)
print(res)