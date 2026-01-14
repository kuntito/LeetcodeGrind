# https://leetcode.com/problems/concatenation-of-array/description/

# you're given an array, `firstArray`
# and want to create another array `secondArray` that's twice as long as `firstArray`

# `secondArray` is essentially two back to back copies of first array.
# for instance, if `firstArray = [1, 2, 3]`
# `secondArray is [1, 2, 3, 1, 2, 3]`

# what's the approach? i'd say create `secondArray`, an empty array
# iterate through first array twice..

# append each element of `firstArray` into `secondArray`
# return `secondArray`

# any edge cases?
# if `firstArray` is empty? still works
# what if `firstArray` is null? we're guaranteed it's a list.

# any other thing? let's find out
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        secondArray = []
        
        for _ in range(2):
            for n in nums:
                secondArray.append(n)
                
        return secondArray