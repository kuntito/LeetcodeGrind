# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

# TODO find the range of the possible solution
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        pass
        # `days` indicates the number of ships you need
        
        # the ship should be large enough to store the largest element
        # without thinking too much, the max the ship can be is the sum of all the elements
        
        # it's looking like a binary search question
        # the range is [max(nums), sum(nums)]
        
        # the `target` is a number such that `target - 1` cannot take all the weights
        
        weights.sort()
        # determine a function that checks if `target` can take all the weights
        
        # the lower bound is the largest weight since the ship has to be big enough to take that weight
        # i did put a lot of thought into the upper bound but it cannot be more than the total of all the ships
        left, right = weights[-1], sum(weights)
        
        # TODO critique the bin search conditions
        while left <= right:
            mid = (left + right) // 2
            
            isMidFit = self.can_take(mid, days, weights)
            isBeforeMidFit = self.can_take(mid - 1, days, weights)
            
            if isMidFit and not isBeforeMidFit:
                return mid
            elif isMidFit and isBeforeMidFit:
                right = mid - 1
            else:
                left = mid + 1
        
        
    # TODO rewrite this function, maximizing the capacity doesn't mean taking the smallest number
    # see `[[3,2,2,4,1,4], 3]`, the answer is `6` but the current implementation says `6` cannot take
    # all ships
    def can_take(self, capacity, ship_count, arr):
        tmp = 0
        count = 0
        for n in arr:
            tmp += n
            
            if tmp >= capacity:
                count += 1
                tmp = n if tmp > capacity else 0
                
            if count > ship_count:
                return False
        
        if tmp > 0:
            count += 1
        
        return count <= ship_count
    
arr = [
    [[1,2,3,4,5,6,7,8,9,10], 5],
    [[3,2,2,4,1,4], 3]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.shipWithinDays(foo, bar)
print(res)