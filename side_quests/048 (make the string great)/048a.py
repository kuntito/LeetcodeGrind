# https://leetcode.com/problems/make-the-string-great/description/

# TODO https://neetcode.io/solutions/make-the-string-great
# 07:07
class Solution:
    def makeGood(self, s: str) -> str:
        arr = []

        # loop through `s`
        for ch in s:
            # append each letter to an array
            arr.append(ch)

            # if the letter added and the previous letter(if any) matches
            # the lowercase and uppercase constraint
            if len(arr) > 1 and self.is_match(arr[-1], arr[-2]):
                # pop them from the array
                arr.pop()
                arr.pop()

        # return the array as a concatenated string
        return "".join(arr)
    
    def is_match(self, one, two):
        a = one.lower() == two.lower()
        b = one != two

        return a and b
    

arr = [
    "s",
    "abBAcC",
    "leEeetcode",
]
foo = arr[-1]
sol = Solution()
res = sol.makeGood(foo)
print(res)