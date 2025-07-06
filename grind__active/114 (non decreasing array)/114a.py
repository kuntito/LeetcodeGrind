# https://leetcode.com/problems/non-decreasing-array/description/

# i want to implement a function that returns a boolean.
# the function takes one argument, an integer array, `nums`.

# i want to find out if the array can become non-decreasing by modifying
# at most one element.

# a non-decreasing array is one where each element is less than or equal
# the next
# i.e. [2, 2, 3] or [2, 3]

# so, i want to find out if i can change at most one element
# to convert `nums` to a non-decreasing array.

# at most one means, it's possible, `nums` is already non-decreasing.

# i think the way to approach this
# count the number of elements that break the pattern
# the pattern for every element, `e` is to be less than the next element

# if this happens more than once, i'd return False
# else, return True after exploring the entire array

# a tweak to my reasoning, it's not enough that the current element is less
# than or equal to the next element, i also have to consider the largest element
# seen so far

# consider, [3, 4, 2, 3]
# based on my initial assumption, the pattern only breaks at 4, 2
# i go from `4` down to `2`, i should change the `2` to at least `4`
# that way i can keep going.

# i think i should actually modify the array
# it would now look like [3, 4, 4, 3]

# this way, it becomes apparent that the pattern breaks again
# from `4` to `3`

# the initial theory was mostly correct, i just had to make sure
# that any changes were reflected in the array

# [3, 4, 2, 3]
# the earlier assumption would have flagged, (4, 2)
# but since, i didn't change it, the array would remain as [3, 4, 2, 3]

# and when i check `2` against `3`, there are no issues

# in other words, i want to iterate from index `1` till the end
# i'd compare the curr elem with the previous
# if the current element is less than the previous, i'd update it to be the previous element
# and increment patternBreak

# if patternBreak exceeds `1`, return False

# if the loop finishes, return True

# the assumption breaks again
# consider [4, 2, 3]

# at first iteration,
# curr = 2
# prev = 4

# so i'd update curr to `4`
# changing the array to `[4, 4, 3]`
# which clearly isn't the case

# since the pattern would still break at (4, 3)
# the answer is obvious staring at it, change the `4` to at most a `2`

# and you'd get [2, 2, 3]
# but how do you know when to change the previous element or the current element?

class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        pass
        dim = len(nums)
        
        patBreak = 0
        idx = 1
        while idx < dim:
            curr = nums[idx]
            prev = nums[idx - 1]
            
            if prev > curr:
                nums[idx] = prev
                patBreak += 1
                
            if patBreak > 1:
                return False
                
            idx += 1
            
            
        return True


    
    
arr = [
    [3, 4, 2, 3],
    [4, 2, 1],
    [4, 2, 3],
]
foo = arr[-1]
sol = Solution()
res = sol.checkPossibility(foo)
print(res)