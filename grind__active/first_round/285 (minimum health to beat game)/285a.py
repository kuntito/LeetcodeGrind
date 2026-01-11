# https://leetcode.com/problems/minimum-health-to-beat-game/description/

class Solution:
    def minimumHealth(self, damage: list[int], armor: int) -> int:
        pass
        # what is this question asking?
        
        # we are given an array, `damage`
        # no, we are playing a game with `x` levels
        
        # we're given an array, `damage` that represents the damage we'd receive to complete each level of the game
        
        # damage[0] is the amount of damage we need to pass level `0`
        # damage[1] is the amount of damage we need to pass level `1` and so on and so forth
        
        # we are given an armor, an integer can we can ise to withstand damage at any level
        # however, the armor can only be used once
        
        # if we were to complete the game such that our health never goes below `1` and we use our armor, what's the minimum health we need to start the game
        
        # 
        # i'd say the first question is to find out when best to use the armor
        # because on one hand, we can sum up all the damages and say our health needs to be the total
        
        # but we need to factor in the armor, the armor can take some damage
        # so do we just subtract the armor from the total?
        
        # well, it's possible we don't use the entire armor
        # consider [2, 3] where armor = 4
        # if we sum the total, we get `5`
        # if we subtract the armor, we get `5-4 = 1`
        
        # this would be wrong since the armor was never used completely
        # ideally, the armor would be used for damage `3`
        
        # so our health would need to be at least `2`
        # is that so? if our health is `2`
        # it means we hit zero, we need our health to never hit zero
        
        # in that case we need the `total + 1` after using the armor appropriately
        
        # consider: damage = [2,7,4,3], armor = 4
        # the armor is best used for the greatest number
        
        # in other words, iterate through the array, tracking the total
        # tracking the largest number
        # apply the armor on the largest number
        # and deduct from the total, the amount of the armor used
        # add `1` and c'est fini
        
        highest = 0
        total = 0
        
        for d in damage:
            total += d
            highest = max(highest, d)
            
        # how do i determine how much of the armor is used
        # two cases, the highest is greater than the armor
        # second case the armor >= highest
        
        if highest > armor:
            total -= armor
        else:
            total -= highest
            
        return total + 1
    
arr = [
    [[2,5,3,4], 7],
    [[2,7,4,3], 4],
    [[3,3,3], 0],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minimumHealth(foo, bar)
print(res)