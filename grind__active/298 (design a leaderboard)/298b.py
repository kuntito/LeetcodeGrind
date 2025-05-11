# https://leetcode.com/problems/design-a-leaderboard/description/

# we need a way to order elements such that when we modify the elements
# the order is maintained

# how does a linked list help, if we add a new number, how do we know where it's meant to be?

# forget linked list and do the bruteforce first
# we want to track the scores for all the players
# each player has an id, and their score can be updated or deleted

# we also want to implement a function where we get the top k scores from the leaderboard

# to store the player scores, a hashmap would suffice
# it allows us to modify or delete in O(1) time

# the struggle would be the top k scores
# NB: if this sort of thing happens during the OA, be sure to think out loud
# this is one of those problems where you know the bruteforce solution but also know that it is inefficient and so you try finding the optimal solution from the get go

# the interviewer doesn't know you know the bruteforce, they don't know what you're doing. as far as they're concerned, you're simply a candidate struggling. it's your job to let them know that you know. don't screw this up for yourself.

# back to the problem. once we have our hash map, getting the topK scores is matter of obtaining the values from the hashmap, sorting them in reverse order
# and grabbing the topK scores

# can we use a heap here?
# pure sorting is nlogn
# but heapify is logn
# with heapify, we can simply obtain the first k characters from the top of the heap

# again, you're entertaining distraction
# you know the list would work, don't force something else
# do list first then maybe heap

# for whatever reason, even the bruteforce worked
# also, you need to pay more attention to what the question is asking before you solve a question

# write a line or two about what each function should do based on the question description
from collections import defaultdict
class Leaderboard:

    def __init__(self):
        self.leaderBoard = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.leaderBoard[playerId] += score

    def top(self, K: int) -> int:
        scores = sorted(self.leaderBoard.values(), reverse=True)
        
        return sum(scores[:K])

    def reset(self, playerId: int) -> None:
        del self.leaderBoard[playerId]

