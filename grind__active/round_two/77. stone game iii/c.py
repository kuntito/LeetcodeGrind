# https://leetcode.com/problems/stone-game-iii/

from typing import List

# i'm given one thing.
# a array of integers, `stoneValue`

# each value in the array represents a stone.

# two people, Alice and Bob, are playing a game, a stone game.

# think of the array, `stoneValue`
# as stones lined up.

# on each turn, each player picks stones from the line.

# each player can either:

# take the first stone
# take the first two stones, or
# take the first three stones

# a player's score is determined by the sum
# of the stone values they've gathered.

# whoever has the highest score, wins.

# and my job is to find out who wins if they each play the best move.
# if Alice wins, i'd return "Alice"
# if Bob wins, i'd return "Bob"

# if they end up with equal scores, i'd return "Tie"

# and how would this go?
# at each point, i want to find the best move.

# do i pick one, two, or three stones.
# on the surface, it seems picking three stones would always be the best choice.
# but consider this:

# [1, 2, 3, 4, 100]

# if the first player picks three stones, they'd have 1 + 2 + 3, a total of `6`
# leaving the next player with 4 + 100, a total of `104`

# let's see if the first player has a better move.
# is it two stones?

# if they picked two stones, they'd have 1 + 2, a total of `3`
# and the second player can always pick all three, 3 + 4 + 100, a total of `107`
# an even greater score.

# what if the first player picked one stone?
# well, they'd have a total of one `1`

# and what does the second player do?
# well, they can do one of three things with the remainder of the array
# [2, 3, 4, 100]

# pick 2
# pick 2 + 3
# pick 2 + 3 + 4

# but it wouldn't matter what they picked..
# since the first player is guaranteed to pick the `100` stone at the end.

# in this case, the best move for the first player is to only pick one stone.

# so, the best move requires foresight.
# if i pick this, what's the most my opponent can get?

# and the opponent is faced with the same choice.
# a compelling case for recursion.

# at each step, you want to find out the best move.

# if i pick one, what does my opponent get?
# if i pick two, what does my opponent get?
# if i pick three, what does my opponent get?

# you'd have to explore all three possibilities
# and pick the one where you get the most
# and your opponent gets the least.

# in other words,
# the greatest difference between my pick and my opponents best pick

# let's revisit the earlier example:
# [1, 2, 3, 4, 100]

# if i pick `1`

# what can my opponent do?
# well, they'd be left with [2, 3, 4, 100]
# so they can pick `2`
    #   if they do so.. i'm left with [3, 4, 100]
    #   in this case, it's a no-brainer, since there are three stones
    #   all positive, i can pick all three..

    # if my opponent picks `2`, i get to pick 3 + 4 + 100, a total of `107`
    
    # now, let's pay attention here..
    # i'm exploring the path where i picked `1`
    # my opponent picked `2`
    # allowing me to pick all three numbers, 3 + 4 + 100
    
    # so my total picks become..
    # 1 + (3 + 4 + 100)
    # and my opponent picks 2
    
    # this exploration was triggered after i picked `1`
    # and asked what's my opponents best pick,
    # then i considered where they picked a single stone
    
    # but what this shows is whenever i ask what my opponents best pick is
    # i also get what my best pick is.. after my opponents pick..
    
    # myPick = 1
    
    # opponent'sPick = 2
    # when opponent picks 2, i get 3 + 4 + 100
    
    # these two data points are part of my response..
    # when i ask, what happens when i pick one stone and my opponent picks one stone.
    
    # in other words, the recursive step returns two things.
    # the opponents best pick, and my best pick onwards..
    
    # this was only one path, i pick one, opp picks one, and i pick all three..
    # there's other paths where i pick one, and opp picks two or picks three..
    # let's explore... 

# they can pick 2 + 3
    # if the opp picks 2 + 3, i get to pick 4 + 100
    
# they can pick 2 + 3 + 4 
    # if the opp picks 2 + 3 + 4, i get to pick 100
    
# if we summarise the results for the opp..
    # pick 2, i get 107
    # pick 2+3, i get 104
    # pick 2+3+4, i get 100
    
    # when you work out the differences:
    # 2-107 = -105
    # 5-104 = -99
    # 9-100 = -91
    
    # the opponent's best pick is three stones...
    # this has the largest difference..
    
    # so at this point, i return two things..
    # the opps best pick and my best pick after the opp
    # 9 and 100
    
# i get back to the main call, where i picked `1`
# at this point, my pick becomes
# what the first stone, `1`, in addition to my best pick after the opp

# so, 1 + 100
# and the opps best pick is 9

# so my first set of results is
#   101 and theirs is 9, this is what happens when i pick a single stone.

# then i explore what happens when i pick two stones..
# figure out the best difference and return two things..

# my best pick, and opps best pick
# we know from the earlier destructuring that picking two or three stones
# are worse moves, but we only know that cause we explored it.

# and so the code must follow suit.

# i took a slight shortcut, when i summed up all three stones
# [3, 4, 5]
# this was the right move, but in code, i wouldn't have known to do this.
# because picking the last three stones only makes sense if all three stones
# are non-negative.

# for instance, if i had
# [3, -4, 1]
# picking all three.. would mean a total of `0`
# not exactly the best move..

# picking a single stone would give me a total of `3`
# in essence, always explore all three possibilities.

# pick one, find opps best pick and your best pick after opp, calculate the difference
# pick two, do the same..
# pick three, do the same..

# compare all the differences..
# pick the one with the largest difference.

# for that difference,
# return your total, and opponents total..

# the question mentions Alice always plays first..
# the recursive function returns two scores..

# the first score is for Alice
# the second, Bob..

# you can return the results.

# there seems to be an opportunity for memoization here.
# since at every point i'm doing the same thing.

# pick one, two, three stones, and in each case start another call with the rest of the array
# when done, find the greatest difference..
# return two scores..

# i can memoize on current index.

# TODO is this the most optimal solution?
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        curIdx = 0
        memo = {}
        aliceScore, bobScore = self.explore(curIdx, memo, stoneValue)
        
        if aliceScore > bobScore:
            return "Alice"
        
        if bobScore > aliceScore:
            return "Bob"
        
        return "Tie"
    
    def explore(self, curIdx, memo, stoneValue):
        if curIdx in memo:
            return memo[curIdx]
        
        # so what am i doing..
        # pick one, two, or three stones..
        
        # and how would that go..
        # a for loop?
        
        # write it plainly first..
        # what if you go out of bounds..
        # a loop can help with this..
        
        # set exploration range...
        # as what's less between the number of stones left
        # and the most stones you can pick, `3`
        
        endRange = min(
            curIdx + 3,
            len(stoneValue)
        )
        
        scoresToReturn = None
        
        for idx in range(curIdx, endRange):
            curPick = sum(
                stoneValue[curIdx:idx+1]
            )
            
            oppBestPick, curBestPickAfterOpp = self.explore(
                idx + 1,
                memo,
                stoneValue
            )
            
            bestPickHere = curPick + curBestPickAfterOpp
            if scoresToReturn is None:
                scoresToReturn = bestPickHere, oppBestPick
            else:
                differenceHere = bestPickHere - oppBestPick
                curDifference = scoresToReturn[0] - scoresToReturn[1]
                
                if differenceHere > curDifference:
                    scoresToReturn = bestPickHere, oppBestPick
                    
        if scoresToReturn is None:
            return 0, 0
        
        memo[curIdx] = scoresToReturn
        return memo[curIdx]
            
arr = [
    [-1, -2, -3],
    [1,2,3,6]
]
foo = arr[-1]
sol = Solution()
res = sol.stoneGameIII(foo)
print(res)