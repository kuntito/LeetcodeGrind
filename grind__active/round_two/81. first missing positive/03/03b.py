from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # step 1. move numbers to index.
        
        for idx, number in enumerate(nums):
            # how do you know to move a number
            # if the index doesn't match the number
            # what does a match look like? `index + 1 == number`
            isMatch = idx + 1 == number
            if not isMatch:
                self.move(idx, number, nums)
            
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
            
                
    def move(self, currentIdx, number, arr):
        # now, how do i move a number
        # well, where should the number go?
        # it should go to the index, `number - 1`
        # this is the `destinationIdx`
        
        # and what does a move look like
        # it means, taking the `number` from it's current position
        # and putting it elsewhere.
        
        # what does taking it from it's current position look like
        # we could place a None at it's current position, to signify absence
        # and placing it is simply, `arr[destinationIdx] = number`
        
        # to remove the number from current position,
        # i need to know what that position is.
        # in other words, i need to pass current index as an argument to `move`
        
        # if i pass current index, i no longer need to pass number
        # since i can deduce it from current index, but i think
        # it makes the solution less readable, so i'd leave it in.
        
        # now, i can move.
        # but hold on, i can't just move any number
        # i need to know if it should be moved.
        # i only want to move numbers in-between `1` and `len(arr)`
        
        shouldMove = 1 <= number <= len(arr)
        if shouldMove:
            # i want to make the current position vacant.
            arr[currentIdx] = 0
            
            # now, i want to move to destination index
            destinationIdx = number - 1
            
            # but what if destination index is occupied
            # move the occupant.
            occupant = arr[destinationIdx]
            occupantCurrentIdx = destinationIdx
            
            self.move(occupantCurrentIdx, occupant, arr)
            
            arr[destinationIdx] = number
        


arr = [
    [3,4,-1,1],
    [2,1],
]
foo = arr[-1]
sol = Solution()
res = sol.firstMissingPositive(foo)
print(res)