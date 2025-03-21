# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        
        while l <= r:
            midCap = (l + r) // 2
            if self.canShip(midCap, days, weights):
                res = midCap
                r = midCap - 1
            else:
                l = midCap + 1

        return res
        

    # `curCap` is a temporary variable representing the capacity
    # of the ship currently being filled
    # whenever it's value becomes negative, it means the ship is maxxed out
    # so we reinitialize it to `maxCap` and decrement the weight that maxxed out the last ship
    def canShip(self, maxCap, days, weights):
        ships, curCap = 1,  maxCap
        
        for w in weights:
            if w >  maxCap:
                return False
            
            curCap -= w
            if curCap < 0:
                ships += 1
                curCap =  maxCap - w
        return ships <= days
    
arr = [
    [[3,2,2,4,1,4], 3],
    [[1,2,3,4,5,6,7,8,9,10], 5],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.shipWithinDays(foo, bar)
print(res)