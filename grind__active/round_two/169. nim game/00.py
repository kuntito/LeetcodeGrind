class Solution:
    def canWinNim(self, n: int) -> bool:
        isMyTurn = True
        
        
        # but how exactly would you write this
        # pick one stone
        # see what happens when the next person picks another stone.
        # so you need a variable to know what person it is.
        # and how many stones left.
        # the end point is when you exhaust the stones
        # on your turn
        # and you can just return True
        # at that point.
        
        # yeah, but how would that work?
        # imagine, it's four stones.
        # you pick one.
        # they pick three.
        # they win.
        # what do they return?
        return self.explore(isMyTurn, n)
        
        
    def explore(self, isMyTurn, stonesLeft):
        # pick 1.
        if stonesLeft <= 3:
            return isMyTurn
        
        res = self.explore(not isMyTurn, stonesLeft - 1)
        if res:
            return res
        
        res = self.explore(not isMyTurn, stonesLeft - 2)
        if res:
            return res
        
        return self.explore(not isMyTurn, stonesLeft - 3)
    
    
arr = [
    4,
    2,
    1,
]
foo = arr[-1]
sol = Solution()

res = sol.canWinNim(foo)
print(res)