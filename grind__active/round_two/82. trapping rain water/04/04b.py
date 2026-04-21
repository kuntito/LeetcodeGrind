from typing import List


# TODO rewrite simply
class Solution:
    def trap(self, height: List[int]) -> int:
        # the idea with Navdeep's solution is you're making an informed decision at each pointer
        
        # you'd place two pointers at the penultimate ends
        # i.e. height[1] and height[-2], if you use Python.
        
        # then, you'd initialize `maxLeft` and `maxRight`
        # but the part he leaves out is max left and max right are dependent on whose asking.
        
        # the left pointer, the one that starts out at height[1]
        # is what owns `maxLeft`, it doesn't know it's max right.
        
        # likewise, the right pointer, the one that starts out at height[-1]
        # is what owns `maxRight`, it doesn't know it's max left.
        
        # so the question at each iteration is
        # which of these pointers knows enough to say how much water it can store.
        
        # the logic here is:
        # for any pointer, 
        # i know the max to one side, 
        # and a maybe max to the other side
        
        # but the interesting case is, if the maybe max to the other side
        # is greater than the max i know.
        
        # it means, the most i can store at my current position
        # is dependent on the max i know.
        
        # why is this the case, let's make this concrete with an example
        # [2, 1, ...., 3]
        # i'm dealing with the left pointer at position `1`
        
        # at this point, i know my max left is `2`
        # and i also know, my max right might be `3`
        
        # but i'm not sure.
        # but i don't need to be sure.
        
        # if i know my max left is `2`
        # and i know for sure, there's a greater number than `2` on my right side
        # it means, `2` is the limiting factor for my storage.
        # it wouldn't matter what else happens on the right.
        
        # i know i can't pass `2`
        # and so, at that point, i can determine the water storage and move the pointer along.
        
        
        # the converse is not true, where if the max i'm unsure of is less than the one i'm sure of.
        
        # consider
        # [2, 1, ... 1]
        # and i'm still at position `1` with the left pointer
        # i know for a fact, the max left is `2`
        
        # but the maybe max right is `1`
        # but i'm not sure, there could be a number within the ... that can match my max left.
        
        # so it's not safe to determine how much water i can store here.
        
        # so the variables are serving two purposes, for the left pointer
        # it's max left
        # for the right pointer, it's maybe max left
        
        # and this is why it gets confusing.
        # perhaps, if i unpack it, it's simpler.
        
        dim = len(height)
        leftIdx, rightIdx = 0, dim - 1
        
        # for left pointer
        forSureMaxLeft = height[leftIdx]
        maybeMaxRight = height[rightIdx]
        
        # for right pointer
        forSureMaxRight = height[rightIdx]
        maybeMaxLeft = height[leftIdx]
        
        # to skip the first and last numbers
        leftIdx += 1
        rightIdx -= 1
        
        totalStorage = 0
        while leftIdx <= rightIdx:
            # the condition that allows me to be sure is
            # if maybeMax is greater than forSureMax
            # i can proceed the index.
            
            
            # for leftIdx
            canLeftProceed = maybeMaxRight > forSureMaxLeft
            if canLeftProceed:
                totalStorage += max(
                    0,
                    forSureMaxLeft - height[leftIdx]
                )
                
                forSureMaxLeft = maybeMaxLeft = max(
                    forSureMaxLeft,
                    height[leftIdx]
                )
                
                leftIdx += 1
            else:
                # if left can't proceed, it's either right can proceed
                # or nothing can happen.
                
                # either way, we're good to move right
                totalStorage += max(
                    0,
                    forSureMaxRight - height[rightIdx]
                )
                
                forSureMaxRight = maybeMaxRight = max(
                    forSureMaxRight,
                    height[rightIdx]
                )
                
                rightIdx -= 1
                
        return totalStorage
    

arr = [
    [0,1,0,2,1,0,1,3,2,1,2,1],
]
foo = arr[-1]
sol = Solution()
res = sol.trap(foo)
print(res)
