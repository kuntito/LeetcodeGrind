# https://leetcode.com/problems/hand-of-straights/description/

import heapq

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        cards_map = {}

        for c in hand:
            cards_map[c] = cards_map.get(c, 0) + 1

        minHeap = list(cards_map.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for card in range(first, first + groupSize):
                if card not in cards_map:
                    return False
                
                cards_map[card] -= 1
                if cards_map[card] == 0:
                    if card != minHeap[0]:
                        return False
                    else:
                        heapq.heappop(minHeap)

        return True


arr = [
    [[1,2,3,6,2,3,4,7,8], 3],
    [[1,2,3,4,5], 4],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.isNStraightHand(foo, bar)
print(res)