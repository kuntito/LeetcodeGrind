# https://leetcode.com/problems/stone-game-iii/

from typing import List

# i'm given a list of integers, `stoneValue`

# two people, Alice and Bob
# take turns playing a game.

# on each turn, 
# each person can take 1, 2 or 3 stones from the list
# each element of `stoneValue` represents a stone.
# or rather, the value of a stone.

# the score of each player
# is the sum of the stone values they picked.

# the objective of the game is to end with the highest score.
# however, the game could end in a tie.

# Alice always starts first.
# Each player starts with a score of `0`

# my job is to find who wins..
# Alice or Bob, if each player plays their best hand.

# i'd return "Alice" if Alice wins, 
# "Bob", if Bob wins
# and "Tie" if neither win.

# so, how would this go?
# at each point, i want to find the best play.

# do i pick 1, 2 or 3 stones. 
# on the surface, it seems 3 stones would always be the best choice
# but consider:

# stoneValue = [1, 2, 3, 4, 100]
# if i pick three stones here: (1, 2, 3)
# this guarantees the next person wins.

# since, they can pick 4 and 100.

# in this case, i'm better off picking one stone.
# this way, no matter what the next person picks
# i'm guaranteed to pick the `100`

# in other words, the best pick is determined by the future picks.
# the future picks of both me and my competitor.

# so, how would this go?
# thing is, i don't know what the best pick would be until i approach
# the situation.

# if i pick one stone, i need to know what happens, if my opp
# picks one or two or three..

# now, it's sounding like i need to know the best play at each position.
# each position has me considering the same things.

# so, i can cache this.

# but how would the code go?
# let's go back here..
# `stoneValue = [1, 2, 3, 4, 100]`

# if i pick `1`
# i'd start a recursive call, the question is 
# what's the best play for the rest of the array, [2, 3, 4, 100]

# here.. i'd have to pick one stone first, `2`
# then another recursive call..

# here, i'd have [3, 4, 100]
# at this point, my best play is to pick everything.

# INSIGHT ONE: 
# if three or less remaining cells, pick all the cells.

# okay.. now i return 3 + 4 + 100 to the parent call where i picked `2`
# the reports is..
# if you pick `2`, your opp gets `107`

# okay, what if i pick two stones, `2` and  `3`
# then your opp gets `4 + 100` = 104
# if you pick a total of `5`, your opp gets a total of `104`

# not good, but better than the last..

# and my last play, if i pick three stones..
# 2 + 3 + 4, i'd have a total of `9`
# and my opp gets `100`
# still not good, but this is the best i can do here..

# the conclusion is, my best play here..
# is picking 9 and my opp gets 100

# so what do i return
# return the value of your best play

# so i return 9 to the parent call, where i picked `1`
# i'd bring back the array to refresh my mind:

# `stoneValue = [1, 2, 3, 4, 100]`
# now, i know, if i pick `1`
# the best my opponent can get is `9`

# but i'm not done..
# i want to also know, what i can pick, after my opps best play
# in this case, i can pick `100` after my opp does his worst.

# so i'd have 1 + 100, and they'd have 9
# so each recursive call returns two things..
# the best play at that point, and the corresponding opponent play..

# so i should have returned `9` and `100`
# so the conclusion would have been, if i pick one stone..
# i'd get `1 + 100` and my opponent would get `9`
# `101` vs `9`

# okay..
# next up what if i pick two stones.. `1 + 2`
# i'd have `3`

# my opponent will be left with the array.. [3, 4, 100]
# they can pick everything.. and would have.. 107
# if i pick two stones..

# i'd have `3`, my opp has `107`
# that's not the best

# and my third choice, if pick three stones..
# i'd have 1 + 2 + 3, i'd have 6
# my opp is left with the array.. [4, 100]
# and would have 104

# if i pick three stones..
# i'd have 6, my opp has 104

# when i line up my options

# pick one
#  101 vs 9
# pick two
#  3 vs 107
# pick three
#  6 vs 104

# it's apparent, my best bet is to pick one..
# but how do i come to this conclusion..

# it's glaring, but code doesn't deal with glares..
# how can you summarize this mathematically

# i'm thinking difference..
# with each pick, i'd get two values
# my final value, my opps value..

# i'd get the difference..  
# compare all the differences between picks..
# and pick the highest one..

# error, my INSIGHT ONE was wrong..
# if you have an array of three or less elements
# you don't want to pick all the elements..

# because, what if they're negative..
# [-1, -2]
# you'd be picking everything..

# need to rewrite this..

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        aliceScore, bobScore = self.explore(stoneValue)
        
        if aliceScore > bobScore:
            return "Alice"
        elif bobScore > aliceScore:
            return "Bob"
        
        return "Tie"
    
    def explore(self, stoneValue):
        if len(stoneValue) <= 3:
            return sum(stoneValue), 0
        
        bestPlay = None
        
        # if pick one
        for pick in range(1, 4):
            currStoneVal = sum(stoneValue[:pick])
            
            oppBestPlay, myBestPlayAfterOpp = self.explore(
                stoneValue[pick:]
            )
                        
            bestPlayAtPick = currStoneVal + myBestPlayAfterOpp
                        
            if bestPlay is None:
                bestPlay = (
                    bestPlayAtPick,
                    oppBestPlay
                )
            else:
                absDiffCurr = bestPlay[0] - bestPlay[1]
                absDiffAtPick = bestPlayAtPick - oppBestPlay
                
                if absDiffAtPick > absDiffCurr:
                    bestPlay = (
                        bestPlayAtPick,
                        oppBestPlay
                    )
                    
        return bestPlay
    
arr = [
    [-1, -2, -3],
    [1,2,3,6]
]
foo = arr[-1]
sol = Solution()
res = sol.stoneGameIII(foo)
print(res)