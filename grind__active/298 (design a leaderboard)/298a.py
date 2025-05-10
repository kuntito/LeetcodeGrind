# https://leetcode.com/problems/design-a-leaderboard/description/

# we want to create a leaderboard such that we can the top k scores at any point

# we need a way to track players and scores, i'm thinking hashmap
# but how do you get the top k scores from a hashmap?

# a heap maybe?
# but the player's scores could update at any time, would i have to heapify every time the player's score changes

# the problem is how can you maintain the order when the scores can change?
# let's start with the bruteforce, for each player, store their details in a hashmap

# playerId -> [playerScore]
# the value is intentionally a list so that, we can access the player's score by reference

# we place the value into a maxheap and whenever we want `top`
# we heapify and get the top 5 then add them back?

# this seems very inefficient, how about a linked list
# to be fair, it seems i'm reaching

# let's use a max heap that never exceeds len 5. the idea here is to add scores to the heap until it's full, once it is we only add new scores, if it's greater than the max. this way the heap always contains the top 5 scores.

# when we modify a player's score, we check if we're modifying an existing score in the heap, if we are we modify accordingly, this bit deserves it's own logic.

import heapq
class Leaderboard:

    def __init__(self):
        self.maxHeap = []
        self.playerMap = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.playerMap[playerId] = score
        
        if len(self.maxHeap) < 5:
            heapq.heappush(self.maxHeap, -1 * score)
        else:
            pass

    def top(self, K: int) -> int:
        return sum(self.maxHeap)

    def reset(self, playerId: int) -> None:
        pass
    
