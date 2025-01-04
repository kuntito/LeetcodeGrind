# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            left_ch = s[left]
            if not left_ch.isalnum():
                left += 1
                continue

            right_ch = s[right]
            if not right_ch.isalnum():
                right -= 1
                continue

            if left_ch.lower() != right_ch.lower():
                return False

            left += 1
            right -= 1

        return True

arr = [
    "A man, a plan, a canal: Panama",
    "race a car",
    " ",
]

foo = arr[-1]
sol = Solution()
res = sol.isPalindrome(foo)
print(res)