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
        left, right = weights[-1], sum(weights)
        
        # TODO critique the bin search conditions
        while left <= right:
            mid = (left + right) // 2
            
            valid_mid = self.can_take(mid, days, weights)
            beforeMid = self.can_take(mid - 1, days, weights)
            if valid_mid and not beforeMid:
                return mid
            elif not valid_mid:
                left = mid + 1
            else:
                right = mid - 1
        
        
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
        
        return count == ship_count
    
arr = [
    [[1,2,3,4,5,6,7,8,9,10], 5],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.shipWithinDays(foo, bar)
print(res)