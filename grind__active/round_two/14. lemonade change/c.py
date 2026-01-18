# https://leetcode.com/problems/path-with-minimum-effort/description/

from typing import List

# omo, just watched neet code's video on it..
# thinking about the situation really simplifies the problem..
# the bills are either 5, 10 or 20...

# the lemonade is always 5, and the customer only buys one..
# if i get 5, no change
# if i get 10, change is 5
# if i get 20, change is 15

# in essence, i would only ever need to give a 5 dollar change
# or a 15 dollar change...

# if it's 5 dollar change, it's basic..
# if it's 15 dollar.. it's a situation { here's where i ran into problems earlier }..

# my thinking was if i had three fivers and one tenner..
# would i rather give the customer three fivers
# or give them a tenner and a fiver..

# but with the constraints of the question, the answer becomes obvious
# i can only give two kinds of change, 5 or 15..
# if i gave the customer three fivers, if i need a five later on
# i wouldn't have it..
# however, if i gave them a tenner and one fiver, i keep my fivers when i need them later..

# there's no situation where i need a tenner and multiple fivers can't help me
# however, there's many situations where i need a fiver and multiple tens can't help me..

# always take the tens first..
# that said, i should be able to write a solution here..

# use a dict to track the notes, the fives and the tens
# no need to track the twenties, since, the highest bill i can receive is 20
# their change, by definition has to be less..

# so track both values, fives and tens..
# on each transaction, i want to store any fives or tens received..

# then write a helper function to check the till and return change
# and if i don't have any change, return False

# else, iterate through and return True

# i didn't specify to only check for change if there's change to be paid
# i.e. change > 0

# and also didn't set the till to defaults i.e. { 5: 0, 10: 0}
# why would i need this, the giveChange method checks for fives..
# if from the jump, customer gives me a ten, and i check for fives..
# this would cause an Key Error.. 

# fixed that and ran into another bug..
# my logic was sound the implementation was wrong..
# i meant to check if the till had at least one five
# and  wrote `notes[fives] > 1`

# instead of `notes[fives] >= 1` or `notes[fives] > 0`
# to be fair, it's easier to read the latter `>=`
# it naturally translates from english to code, greater than or equal to 1
# than saying greater than zero to mean one or more..

# also, need to write give Change more efficiently



class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = {5:0, 10: 0}
        
        lemonadePrice = 5
        for n in bills:
            notes[n] = notes.get(n, 0) + 1
            
            change = n - lemonadePrice
            if change and not self.giveChange(change, notes):
                return False
            
        return True
    
    # change is either 15 or 5
    def giveChange(self, change, notes):
        fives = 5
        tens = 10
        if change == 5 and notes[fives]:
            notes[fives] -= 1
            return True
        
        if change == 15:
            if notes[tens] and notes[fives] >= 1:
                notes[tens] -= 1
                notes[fives] -= 1
                return True
            elif notes[fives] >= 3:
                notes[fives] -= 3
                return True
        return False
    

    
arr = [
    [5,5,5,10,20],
    [5,5,5,5,10,5,10,10,10,20],
]
foo = arr[-1]
sol = Solution()
res = sol.lemonadeChange(foo)
print(res)