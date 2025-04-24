# https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/

class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        pass
        # you want to spread `k` across the integers the nums
        # you can spread `k` however you want
        # but you want to find out the configuration
        # that gives the highest frequency of a single number
        # 
        
        # consider: [1, 2, 4] where k = 5
        # if you put all of `k` on `nums[0]`
        # you'd have [6, 2, 4]
        # if you put everything on `nums[1]`
        # you'd have [1, 7, 4]
        
        # the ideal is to place, `3` on nums[0]
        # and `2` on [1]
        # to form [1 + 3, 2 + 2, 4] = [4, 4, 4]
        
        # bruteforce, i'm thinking sort all the numbers
        # take turns 