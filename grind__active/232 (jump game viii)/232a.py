# https://leetcode.com/problems/jump-game-viii/description/

class Solution:
    def minCost(self, nums: list[int], costs: list[int]) -> int:
        pass
        # you can jump forward if:
        # the value at the forward index is greater than or equal to your value and all the intervening values are less than your value
        
        # i.e. [3, 2, 4]
        # you can jump from value `3` to value `4`
        # since `4` >= `3` and the intervening value `2` is less than `3`
        
        # you can jump forward if:
        # the value at the forward index is less than your value and all the intervening values are greater than your value
        # i.e. [2, 4, 1]
        # you can jump from value `2` to value `1`
        # since `1` is less than `2`
        # and the intervening value `4` is greater than it
        
        # treat both scenarios separately, and return the minimum of both
        
        # it's looking like a dp problem
        # for type 1
        # we're jumping from small to big
        # with everything in between less than small
        
        # so we'd need to track the smallest index seen before the item??