# https://leetcode.com/problems/maximum-size-of-a-set-after-removals/description/


# i want to iterate through both arrays
# i'd have created a result set, `res`

# with each iteration, i'd have two numbers
# i'd add each unique one to `res`
# and break the loop if `len(res) == n/2`

# TODO i've misread the question.
# i want to remove n/2 elements from each array
# while forming a set with the remainder elements
# i want to form the largest set possible.

# in which case, what elements do i remove?
# let's try removing the elements common to both sets

# i think my old idea can be repurposed.
# i want unique elements from each group.
# doesn't really matter which one i remove
# so long as it's unique and the result is less than size `n`.


class Solution:
    def maximumSetSize(self, nums1: list[int], nums2: list[int]) -> int:
        pass
        res = set()
        maxElems = len(nums1)
        
        for a, b in zip(nums1, nums2):
            res.add(a)
            if len(res) == maxElems:
                break
            res.add(b)
            if len(res) == maxElems:
                break
            
        print(res)
        return len(res)

            
arr = [
    [[1, 2, 1, 2], [1, 1, 1, 1]],
    [[1,2,3,4,5,6], [2,3,2,3,2,3]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.maximumSetSize(foo, bar)
print(res)