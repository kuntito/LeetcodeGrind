# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

# i want to implement a function, `hasAllCodes`, and this function returns a boolean.
# `hasAllCodes` takes two strings, `s` and `k`.

# i want to return True, if every substring of s

# i want to explore every substring in `s` of size `k`
# and want to return True if every substring-

# i think i have it all wrong.
# consider a string of size, `k`
# let's call it `kString`

# each character in `kString` can either be `0` and `1`
# we want to explore every combination of 0s and 1s
# and return True if every combination exists as a substring in `s`

# for instance,
# s = "00110110"
# k = 2

# since k is `2`, our substring can either be "00", "01", "10" or "11"
# and each one of those substrings exist in `s`

# "00" exists at index `0`
# "01" exists at index `1`
# "10" exists at index `3`
# "11" exists at index `2`

# now that i understand the question, how do i solve it?
# off the dome, i'd say, determine all the kStrings and check if they exist in `s`

# i recognize, this would be incredibly inefficient
# but it should work on small strings.


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        pass
        self.kStrings = []
        self.populateKStrings(k, [])
        
        print(self.kStrings)
        
    def populateKStrings(self, k, tempArr):
        # how would i get all k strings
        # i'm thinking recursion and backtracking
        
        # for each function call, i'd need an array
        # to store the k elements
        # i'd need a global array to store kstrings too
        if k == 0:
            self.kStrings.append(
                "".join(tempArr)
            )
            return
        
        tempArr.append("1")
        self.populateKStrings(k-1, tempArr)
        tempArr.pop()
        
        tempArr.append("0")
        self.populateKStrings(k-1, tempArr)
        tempArr.pop()
        
    
arr = [
    ["0110", 1],
    ["00110110", 2],
]
foo, bar = arr[-1]
sol = Solution()
sol.hasAllCodes(foo, bar)