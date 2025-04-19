# https://leetcode.com/problems/two-sum-less-than-k/description/

class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        pass
        # in the array, we want to find two indices such that their sum is less than k
        # and we want to find the largest pair sum less than k
        
        # i'd say, sort the list
        # and use two pointers, starting at both extremes
        # left and right
        
        # TODO not sure why it would work though
        left, right = 0, len(nums) - 1
        
        nums.sort()
        
        maxLess = -1
        while left < right:
            uno, dos = nums[left], nums[right]
            
            total = uno + dos
            if total >= k:
                right -= 1
            else:
                if total > maxLess:
                    maxLess = total
                
                left += 1
                
        return maxLess
    
arr = [
    [[34,23,1,24,75,33,54,8], 60],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.twoSumLessThanK(foo, bar)
print(res)
