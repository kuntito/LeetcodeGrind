# https://leetcode.com/problems/path-with-minimum-effort/description/

from typing import List


# right, so what we doing?

# there's a lemonade stand, each lemonade costs $5.

# there's a queue of customers, and they only pay with five dollar, ten dollar and twenty dollar bills i.e.

# * 5
# * 10
# * 20

# and i must provide them the right change. i must note that i don't have any change from the jump.

# given an array, `bills`, that represents how much each customer has..

# i want to find out if it's possible to give every one their change, i'm returning a boolean..

# in simpler terms, i'm given an array, `bills`, containing integers, `5`, `10` or `20`.

# the integers in `bills` represent the amount customers pay for lemonade. each lemonade is $5, the aim of this challenge is to find out if, taking the customer bills in order, i can give every body their correct change.

# i start out with zero change..
# off the dome, i'd say iterate through the array
# keep track of how much change you have..

# for each customer, calculate their change, see if you can pay it..
# if you can't, stop the iteration by returning False

# else, finish the iteation and return True..
# okay, so how would that go?

# what is change? change is really how much i have in the till.
# the first person needs to pay with $5 else, the whole thing crumbles..

# nonetheless, on each iteration, i'd subtract $5 from customer amount, whatever is left is their change.

# i'd add what they paid me to the the till.
# if i need to give customer change, i see if the till can handle it
# else.. game over.

# okay, this is too simplistic..
# i don't think it would work, because i'm not considering the type of notes in the till
# if i have a $10 note in the till and the customer needs $5 change..

# my earlier approach would say i have change, but in reality i don't
# i need a way to map how much i have in the till
# and if i can give the customer change..

# this has "changed" the game significantly..
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        till = 0
        
        for am in bills:
            change = am - 5
            till += 5
            
            till -= change
            if till < 0:
                return False
            
        return True