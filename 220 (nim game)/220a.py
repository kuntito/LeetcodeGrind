class Solution:
    def canWinNim(self, n: int) -> bool:
        # brute force approach
        # use a recursive function that takes
        # count, stonesLeft
        # an even count represents you
        # an odd count represents your neighbour
        # take turns alternating it

        return self.explore(0, n)

    def explore(self, count, stonesLeft):
        if stonesLeft <= 3:
            return count % 2 == 0
        

        for i in range(1, 4):
            if i > stonesLeft:
                break
            res = self.explore(count + 1, stonesLeft - i)
            if res:
                return True

        return False
    

arr = [
    4,
    1,
]
foo = arr[-1]
sol = Solution()
res = sol.canWinNim(foo)
print(res)