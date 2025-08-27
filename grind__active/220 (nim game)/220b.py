# https://leetcode.com/problems/nim-game/description/

# right, what is this joint? i want to implement a function,`canWinNim`, that takes an integer `n` and returns a boolean.

# but what happens in between? `nim` is a game and the way it's played is this:

# there's two players and a heap of stones. each player takes turns removing some stones from the heap.

# the one who removes the last stone is the winner. the constraint is
# each person can only remove `1` to `3` stones. they can remove one, two or three stones in one turn.

# `n` represents the starting number of stones in the heap. if both players play optimally, return a boolean indicating if the player who starts first can win the game.

# off the dome, brute force. explore every possibility. see if there's one where the first player wins.

# so, how would this go?
# i'm thinking recursion, we pass arguments, `numStonesToPick`, `currTurn`, `stonesLeft`

# once `stonesLeft` hits zero, we return a boolean representing `currPlayerIsStartingPlayer` 
class Solution:
    def canWinNim(self, n: int) -> bool:
        pass
        
        # we'd start at `1` and increment on consequent recursive calls, once we hit a `3`, we swap the turns and reset `stonesToPick = 1`
        stonesToPick = 1
        
        # True, if first player, False, otherwise
        currTurn = True
        
        stonesLeft = n
        
        return self.explore(stonesToPick, currTurn, stonesLeft)
    
    def explore(self, stonesToPick, currTurn, stonesLeft):
        # there a base case? well, i'd check for `stonesLeft == 0`
        # after every pick, this way, we know immediately when we hit zero
        
        # what if you want to pick more stones than stones left,
        # i think the check already handles that.
        
        # we're guaranteed at least one stone, so if i pick that
        # on the first recursive call, the check would reveal i'm at the end and then i can return
        
        stonesAfterPicks = stonesLeft - stonesToPick
        if stonesAfterPicks == 0:
            return currTurn
        
        # i don't think your point earlier is correct. if i check
        # that `stonesAfterPicks > 0`, this doesn't necessarily mean there's enough stones to pick on the next iteration
        
        # i could have stonesAfterPicks = 1 and stonesToPick = 2
        # TODO