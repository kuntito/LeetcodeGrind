# https://leetcode.com/problems/split-array-largest-sum/description/

# TODO deep wagwan in `191a.py`, merge with this one then deep neet
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        pass
        # you want to split `nums` into `k` contiguous chunks
        # there's multiple ways to split it
        # but you want to find the one with the lowest largest sum
        
        # for example,
        # say we wanted to split `[2, 3, 6]` into two chunks
        # we could do `2` and `3, 6`
        
        # OR
        
        # we could do `2, 3` and `6`
        
        # looking at both splits,
        # in `2` and `3, 6` => the array sums are `2` and `9`, largest is `9`
        # in `2, 3` and `6` => the array sums are `5` and `6`, largest is `6`
        
        # if we determine, the largest size a chunk can be
        # the brute force is to try every configuration
        # determine the largest size
        # and track the lowest largest
        

    
arr = [
    [[7,2,5,10,8], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)