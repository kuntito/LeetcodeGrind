# https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/

from collections import Counter
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        pass
        # you want to spread `k` over as many numbers as possible
        # such that you obtain the most frequent element
        
        # does `nums` contain duplicates
        # possibly, let's get sorted set of unique elements
        

        # it's a moving sliding window problem
        
        # you want to sort the unique elements
        # have a sliding window that's at least 2 elements long
        
        # uno, dos
        # `dos` is always at the largest element in the array
        # since we're dealing with unique elements, it's bound to be unique
        # we then find what we need to add to every element in the window
        # to each the largest element `uniques[dos]`
        # if the added number is <= k
        # we track the length of the window as the current length
        
        # the number added number is > k, we move left
        # and update added number until it is <= k
        # and we track the window as current length
        
        # do we really need uniques??
        
        nums.sort()
        
        maxFreq = 1
        winSum = nums[0]
        left = 0
        dim = len(nums)
        for dos in range(1, dim):
            currNum = nums[dos]
            winSum += currNum
            
            # if all the numbers in the window are equal, we'd have a ceiling sum
            dist = (dos - left) + 1
            ceilingSum = currNum * dist
            
            neededSum = ceilingSum - winSum
            while neededSum > k:
                winSum -= nums[left]
                left += 1
                
                dist = (dos - left) + 1
                ceilingSum = currNum * dist
                neededSum = ceilingSum - winSum
                
            maxFreq = max(maxFreq, (dos - left) + 1)
            
        return maxFreq
    
    
arr = [
    [[1,2,4], 5],
    [[1,4,8,13], 5],
    [[3,9,6], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.maxFrequency(foo, bar)
print(res)