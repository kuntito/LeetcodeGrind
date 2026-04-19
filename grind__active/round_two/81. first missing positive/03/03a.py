from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # step 1. move numbers to index.
        
        for idx, number in enumerate(nums):
            # how do you know to move a number
            # if the index doesn't match the number
            # what does a match look like? `index + 1 == number`
            isMatch = idx + 1 == number
            print(number)
            if not isMatch:
                self.move(number, nums)
            
        # step 2. find the first number not at it's index 
        for idx, number in enumerate(nums):
            # what does a number not at it's index look like
            # `idx + 1 != number`
            # what does this mean?
            # i expect the number at `idx` to be equal to `idx + 1`
            # if this isn't the case, `idx + 1` is the smallest positive integer.
            
            expectedNumber = idx + 1
            isNotAtIndex = expectedNumber != number
            if isNotAtIndex:
                return expectedNumber
            
        # if i never find the expected number
        # my answer is `arraySize + 1`
        return len(nums) + 1
            
                
    def move(self, number, arr):
        # now, how do i move a number
        # well, where should the number go?
        # it should go to the index, `number - 1`
        
        # but first, we need to determine if the number should even move
        # keep in mind, we only want to move numbers between `1..arraySize`
        
        shouldMove = number in range(1, len(arr))
        if shouldMove:
            # then we move, but what if it's occupied
            # well, we should move the occupant to
            # so recursion.
            
            destinationIdx = number - 1
            occupant = arr[destinationIdx]
            
            self.move(occupant, arr)
            
            arr[destinationIdx] = number


arr = [
    [3,4,-1,1],
]
foo = arr[-1]
sol = Solution()
res = sol.firstMissingPositive(foo)
print(res)