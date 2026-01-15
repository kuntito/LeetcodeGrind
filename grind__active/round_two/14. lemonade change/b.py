# https://leetcode.com/problems/path-with-minimum-effort/description/

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # back to the drawing board...
        # i need a way to store the notes i'm being given..

        # a dictionary is appropriate for this..
        # so i know how much of each note i have
        notes = {}
        for n in bills:
            notes[n] = notes.get(n, 0) + 1
            
            change = n - 5
            
            # the question is now, how do i decide
            # what notes to give the customer as change..
            # what do you mean?
            # since the bills are 5, 10, 20
            # customers change is either 5 or 15
            # so, say i want to give customer 15
            
            # and the till, i have 3 fivers, one tenner
            # how do i know if to give them one tenner and a fiver
            # or all three fivers..
            # since i don't know who or what comes next..
            # it's not clear what the best approach is...
            
            # off the dome, i could brute force it..
            # this would change it to a recursive function
            
            # where at each call, you want to see if you can pay
            # the current customer their change..
            # you'd basically try out every possibility
            
            # and how would writing that work..
            # you'd go through each note, deduct it from customer..
            
            # i don't have the intuition for this, in the spirit of speed
            # i'd better watch a video..