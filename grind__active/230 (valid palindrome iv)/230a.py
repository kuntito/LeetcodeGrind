# https://leetcode.com/problems/valid-palindrome-iv/description/

class Solution:
    def makePalindrome(self, s: str) -> bool:
        # two pointers, `left` and `right`
        # if the values at the pointers are equal
        # move the pointers closer
        # if the values differ, this is an opportunity for a swap
        # it's either you change the left value or the right value
        
        # it really doesn't matter if you change the left or the right value since a palindrome just needs both values to be equal
        
        
        count = 0
        left, right = 0, len(s) - 1
        while left <= right:
            leftValue = s[left]
            rightValue = s[right]
            
            if leftValue != rightValue:
                count += 1
            
            left += 1
            right -= 1
            
        return count <= 2

    
arr = [
    "abcdef",
    "aa",
    "abcdba",
]
foo = arr[-1]
sol = Solution()
res = sol.makePalindrome(foo)
print(res)