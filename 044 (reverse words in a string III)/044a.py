# https://leetcode.com/problems/reverse-words-in-a-string-iii/

# TODO https://neetcode.io/solutions/reverse-words-in-a-string-iii
class Solution:
    def reverseWords(self, s: str) -> str:
        # convert `s` to an array, `s_arr`
        
        # TODO, this description no follow
        # you convert `s` into an array of characters then
        # you're track left and right and every time you find a space
        # you reverse the elements in that range
        # and update, left and right
        
        
        # two pointers, `left` and `right`
        # `left` moves until it's value is at a non-string char
        
        # then `right` moves and stops when the next char is a string or it reaches the end of the string
        
        # on each cycle of this, use a function `reverse_chars(left, right, s_arr)`
        # to reverse the characters
        # then left = right + 1

        s_arr = list(s)
        left = 0
        right = 0

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