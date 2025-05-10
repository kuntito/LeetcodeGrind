# https://leetcode.com/problems/design-a-leaderboard/description/

# we need a way to order elements such that when we modify the elements
# the order is maintained

# how does a linked list help, if we add a new number, how do we know where it's meant to be?



import heapq
class Leaderboard:

    def __init__(self):
        pass

    def addScore(self, playerId: int, score: int) -> None:

        pass

    def top(self, K: int) -> int:
        return sum(self.maxHeap)

    def reset(self, playerId: int) -> None:
        pass
