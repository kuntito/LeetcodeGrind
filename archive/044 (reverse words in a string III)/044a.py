# https://leetcode.com/problems/reverse-words-in-a-string-iii/

# TODO https://neetcode.io/solutions/reverse-words-in-a-string-iii
class Solution:
    def reverseWords(self, s: str) -> str:
        # convert `s` to an array, `s_arr`
        
        s_arr = list(s)
        left = 0
        right = 0
        
        # the idea is to reverse in-place the chars in the array
        # left index aims to find the first non-string character
        # once found, right index moves onwards till it finds the last char
        # before a space
        # at this point, left index and right index represent the boundaries
        # of a word
        # the word is reversed in-place with a helper function
        # and left index is updated to right index, leftIdx = rightIdx
        
        # and the iteration continues
        # at the end, all words would have been reversed and everyone
        # goes home to their families


        dim = len(s_arr)
        while left < len(s_arr):
            ch = s_arr[left]
            if ch != ' ':
                right = left
                while (right + 1 < dim) and s_arr[right + 1] != " ":
                    right += 1

                self.reverse(left, right, s_arr)
                left = right
                
            left += 1

        return ''.join(s_arr)

    def reverse(self, left, right, arr):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

arr = [
    "Let's take LeetCode contest",
    "ab cd",
]
foo = arr[-1]
sol = Solution()
res = sol.reverseWords(foo)
print(res)