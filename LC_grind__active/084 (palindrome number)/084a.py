# https://leetcode.com/problems/palindrome-number/description/
import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        pass
        # create an array
        arr = []
        # use divmod to get all the digits from behind
        # append all digits to the array
        is_neg = x < 0
        x = abs(x)
        
        while x:
            x, digit = divmod(x, 10)
            # beware of python's behavior (-1 % 10 == 9)
            # for the purpose of this question, it should be -1
            # this should only occur at the last accessed digit
            if x == 0 and is_neg:
                digit = -digit
            arr.append(digit)
            
        # apparently, `-n` reversed is `n-`
        if len(arr) == 1 and is_neg:
            return False
            
        # use two pointers to check if the array is a palindrome
        start, end = 0, len(arr)-1
        while start <= end:
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
            
        return True
    
arr = [
    -121,
    10,
    121,
]
foo = arr[-1]
sol = Solution()
res = sol.isPalindrome(foo)

print(res)