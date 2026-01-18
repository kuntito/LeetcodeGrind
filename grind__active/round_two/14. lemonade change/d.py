# https://leetcode.com/problems/path-with-minimum-effort/description/

from typing import List



# `c.py` works but i wrote an unimpressive function for give change..
# my efficient code is even more inefficient 'ccording to LeetCode runner..

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = {5:0, 10: 0}
        
        lemonadePrice = 5
        for n in bills:
            notes[n] = notes.get(n, 0) + 1
            
            change = n - lemonadePrice
            if not self.giveChange(change, notes):
                return False
            
        return True
    
    # i want to apply recursion
    # first off, if change is 0: return True
    # if change >= 10, and there's a ten, deduct the ten from change
    # deduct the ten from till, call the function again with the new change..
    
    # if it wasn't clear, each recursive call attempts to deduct a ten..
    # if possible it starts another recursive call and returns it..
    # this works, since there's only one instance where.. we want to return 10
    # well, if you return the recursive call and there's no fives.. well return False..
    
    # what if there was fives, deduct the fives and go back..
    # returning once on a valid ten works..
    
    # okay, second line of each rec function is deduct the five from change and from till
    # and start another recursive call..
    
    # what if there's no fives.. return False
    def giveChange(self, change, notes):
        if change == 0:
            return True
        
        if change > 10 and notes[10]:
            notes[10] -= 1
            return self.giveChange(change - 10, notes)
        
        if notes[5] == 0:
            return False
        
        notes[5] -= 1
        return self.giveChange(change - 5, notes)
        

    
arr = [
    [5,5,5,10,20],
    [5,5,5,5,10,5,10,10,10,20],
]
foo = arr[-1]
sol = Solution()
res = sol.lemonadeChange(foo)
print(res)