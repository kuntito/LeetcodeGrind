# https://leetcode.com/problems/valid-palindrome-ii/description/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        pass
        dim = len(s)
        left, right = 0, dim-1
            
        return self.explore(left, right, s, False)
    
    def explore(self, left, right, s, isSkipped):
        if left < 0 or right == len(s): return False

        while left <= right:
            if s[left] != s[right]: 
                if isSkipped:
                    return False
                else:                
                    return self.explore(left+1, right, s, True) or self.explore(left, right-1, s, True)

            left += 1
            right -= 1

        return True
    
arr = [
    "aba",
    "abca",
]
foo = arr[-1]
sol = Solution()
res = sol.validPalindrome(foo)
print(res)

        