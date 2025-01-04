
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            left_ch = s[start]
            if not self.is_alnum(left_ch):
                start += 1
                continue

            right_ch = s[end]
            if not self.is_alnum(right_ch):
                end -= 1
                continue

            if left_ch.lower() != right_ch.lower():
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
        

