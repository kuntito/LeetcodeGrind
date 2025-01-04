# https://leetcode.com/problems/valid-palindrome-ii/description/

# TODO https://www.youtube.com/watch?v=JrxRYBwG6EI
class Solution:
    def validPalindrome(self, s: str) -> bool:
        dim = len(s)
        left, right = 0, dim-1

        while left <= right:
            if s[left] != s[right]:
                return self.explore(left+1, right, s) or self.explore(left, right-1, s)
            left += 1
            right -= 1
            
        return True
    
    def explore(self, left, right, s):
        if left < 0 or right == len(s): return False

        while left <= right:
            if s[left] != s[right]: return False

            left += 1
            right -= 1

        return True
    
arr = [
    "aba",
    "abc",
]
foo = arr[-1]
sol = Solution()
res = sol.validPalindrome(foo)
print(res)

        