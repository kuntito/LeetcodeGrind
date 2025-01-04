# https://leetcode.com/problems/koko-eating-bananas/

import math


def can_finish(val, arr, hours_available):
    hours_left = hours_available
    for idx in range(len(arr)-1, -1, -1):
        if hours_left <= 0: return False

        pile = arr[idx]
        if val >= pile:
            return hours_left - (1 + idx) >= 0

        hours_left -= math.ceil(pile/val)

    return hours_left >= 0


class Solution:
    def minEatingSpeed(self, piles, h):
        if len(piles) > h: return None
        piles.sort()

        min_val = piles[-1]

        left, right = 1, min_val

        while left <= right:
            mid = (left + right)//2
            if can_finish(mid, piles, h):
                min_val = min(mid, min_val)
                right = mid - 1
            else:
                left = mid + 1


        return min_val



piles = [3,6,7,11]
h = 8

piles = [30,11,23,4,20]
h = 5

piles = [30,11,23,4,20]
h = 6

piles = [312884470]
h = 312884469

foo = Solution()
res = foo.minEatingSpeed(piles, h)
print(res)

