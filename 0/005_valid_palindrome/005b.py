
class Solution:
    def isPalindrome(self, s: str) -> bool:
        foo = ''
        for ch in s:
            if ch.isalnum():
                foo += ch.lower()

        return foo == foo[::-1]