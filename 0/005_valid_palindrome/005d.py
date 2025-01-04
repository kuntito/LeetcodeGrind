class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            while start < end and not self.is_alnum(s[start]):
                start += 1
                
            while start < end and not self.is_alnum(s[end]):
                end -= 1

            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1

        return True
    
    def is_alnum(self, ch: str):
        lower_range = range(ord('a'), ord('z') + 1)
        upper_range = range(ord('A'), ord('Z') + 1)
        num_range = range(ord('0'), ord('9') + 1)

        return ord(ch) in lower_range or\
            ord(ch) in upper_range or\
            ord(ch) in num_range

arr = [
    "race a car",
    " ",
    "A man , a plan, a canal: Panama",
    ".,"
]

foo = arr[-1]
sol = Solution()
res = sol.isPalindrome(foo)
print(res)


# used `if` instead of `while` loop
# condition is `start < end`