# https://leetcode.com/problems/contains-duplicate-ii/description/

# i want to find two indices in `nums`, `idxOne` and `idxTwo`, whose absolute difference is <= k
# and also both indices need to have the same value
# i.e. nums[idxOne] == nums[idxTwo]

# i tried a double nested solution, see `a.py`
# it took too long, now i want to optimize.

# at each index, i'm asking the question, is there another index with the next k available indices
# that contain the same value as me.

# this reveals the solution.
# why not store values in a dictionary
# the dict key is the value, the dict value is an array

# that array would represent all the indices that value exists
# then what?
# say k = 2
# and nums = [1, 2, 3, 4, 5, 1]

# the dict would be {1: [0, 5]}
# in this case, i'd have a no since `abs(5-0) > k`

# but what if i had
# k = 2
# nums = [1, 2, 3, 4, 5, 1, 1]
# the dict would be {1: [0, 5, 6]}
# in this case, i'd have a yes..

# in essence, for each value
# i'd want to compare the current index with it's last occurence..
# it's last occurence would be the closest occurence..

# is this True? well, if i iterate from start to finish, yes, this is true
# in essence, i don't even need to store an array, just the last index where the value was found..

# if the absolute diff is matching, voila..
# let's test it..

# i left out the part where we always update the dicts value to the current index
# on each iteration, we check if element exists in dict, if yes, compare with current dict entry
# if match, return True

# else.. leave the if block and update the current index

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        ndict = {}
        
        for currIdx, elem in enumerate(nums):
            if elem in ndict:
                closestIdx = ndict[elem]
                if abs(closestIdx - currIdx) <= k:
                    return True
            
            ndict[elem] = currIdx
        return False
    
arr = [
    [[1,0,1,1], 1],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.containsNearbyDuplicate(foo, bar)

print(res)