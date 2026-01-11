# https://leetcode.com/problems/maximum-size-of-a-set-after-removals/description/

# given two integer arrays,`nums1`, `nums2`, we want to create a set of at most `n` elements

# what's the largest set we can get, assuming we can only take n/2 elements from each integer array.

# i'd say convert both arrays into a set.
# or convert one array into a set.

# it's easier to start with the less efficient solution.
# determine n/2
# convert both arrays into a set

# for each set, iterate through
# adding each unique element to the result set.

# stop, once you hit n/2 or exhaust the array
# do the same for the next array

# TODO i'm wrong
# seems at first pass, i want to add to `res`
# the elements in `foo` not in `bar`
# then target the elements in both
class Solution:
    def maximumSetSize(self, nums1: list[int], nums2: list[int]) -> int:
        pass
        res = set()
        
        self.maxPerArray = len(nums2)/2
        
        setOne = set(nums1)
        setTwo = set(nums2)
        
        self.addToRes(setOne, res)
        self.addToRes(setTwo, res)
        
        return len(res)
        
    def addToRes(self, someSet, res):
        count = 0
        for n in someSet:
            if count == self.maxPerArray:
                break
            
            if n not in res:
                res.add(n)
            
            count += 1
            
arr = [
    [[1, 2, 1, 2], [1, 1, 1, 1]],
    [[1,2,3,4,5,6], [2,3,2,3,2,3]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.maximumSetSize(foo, bar)
print(res)