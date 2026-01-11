# https://leetcode.com/problems/permutation-sequence/


# i want to implement a function, `getPermutation`
# the function takes two integer arguments, `n` and `k`

# the idea is to express `n` as a range of integers
# from `1..n`

# i.e. if `n` is `3`, the list of integers would be [1, 2, 3]
# given this list, we want to determine all it's permutations
# and we want to these permutations to be in order

# and once we have the permutations and their order
# we want to return the kth permutation.

# what would permutations in order look like?
# for our example, `[1, 2, 3]`
# the permutations are:

# "123"
# "132"

# "213"
# "231"

# "312"
# "321"

# i can deduce, the first permuation is the natural order of the list
# "123"

# the second permutation keeps the first number constant and swaps the other two digits
# i'm starting to consider an approach where we break this into smaller problems

# say the first number is "1"
# i want to find out how many different ways i can permute the rest of the list, "23"
# and preprend it with "1"

# it's simple to visualize the permutations of "23"
# since they're only two digits, i'd have "23" and "32"

# hence, "1" + "23" and "1" + "32"

# okay... but how does that explain the other permutations
# "213"
# "231"

# "312"
# "321"

# it's similar in the sense that you start with one digit, permute the other two
# the result here can be obtained by iterating through "123"
# where the current number is the first digit
# and then we permute the other two
# and append their results to the first digit

# this works for a list of three numbers.
# what happens when it's four?

# well, we know what happens when it's three
# it's a matter of doing the same thing,
# iterate through all four numbers
# permutate the other three numbers

# and you can do the same for five, six, seven...etc

# the challenge now, is having selected the first digit
# how do you select the other numbers and permute them
# i don't think i need anything crazy here.

# if i turn the list into a string
# and iterate with index
# i can obtain the current number
# get the previous numbers and the next numbers
# concatenate them and start another recursive function

# and what would the base case look like?
# the base case would be a list of two numbers or a list of one number

# and how do you get the kth value?
# let's get the sequence of permutations first then we'd take it from there

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        pass
        chars = "".join(str(i) for i in range(1, n + 1))        
            
        arr = []
        for idx, ch in enumerate(chars):
            otherChars = chars[:idx] + chars[idx + 1:]
            for nei in self.explore(otherChars):
                arr.append(ch + nei)
                
        for seq in arr:
            print(seq)
            
    def explore(self, chars):
        dim = len(chars)
        if dim == 1:
            return [chars]
        
        if dim == 2:
            f, s = chars
            return [f + s, s + f]
        
        arr = []
        for idx, ch in enumerate(chars):
            otherChars = chars[:idx] + chars[idx + 1:]
            for nei in self.explore(otherChars):
                arr.append(ch + nei)
                
        return arr
        
        
arr = [
    [3, 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.getPermutation(foo, bar)
print(res)