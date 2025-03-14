# https://leetcode.com/problems/hand-of-straights/description/

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        ordered_cards = []
        cards_map = {}

        for c in hand:
            if c in cards_map:
                cards_map[c] += 1
            else:
                cards_map[c] = 1
                ordered_cards.append(c)

        ordered_cards.sort()

        idx = 0
        while len(cards_map) >= groupSize:
            while ordered_cards[idx] not in cards_map:
                idx += 1
            
            card = ordered_cards[idx]
            
            for card in range(card, card + groupSize):
                if card in cards_map:
                    cards_map[card] -= 1
                    if cards_map[card] == 0:
                        del cards_map[card]
                else:
                    return False
                
        return len(cards_map) == 0


arr = [
    [[1,2,3,6,2,3,4,7,8], 3],
    [[1,2,3,4,5], 4],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.isNStraightHand(foo, bar)
print(res)