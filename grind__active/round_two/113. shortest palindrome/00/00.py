class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # i would always be adding characters to to the start
        # i'd pick off characters from the end of `s`
        # and form a pre-string.
        
        # the pre-string is stored in an array.
        # with every character i pick off the end of `s`
        # i'd append to the pre-string.
        
        pre_string = []
        # first, i'd check if `s` is a palindrome
        if self.isPalindrome(pre_string, s):
            return s
        dim = len(s)
        for idx in range(dim-1, -1, -1):
            ch = s[idx]
            pre_string.append(ch)
            
            if self.isPalindrome(pre_string, s):
                return "".join(pre_string) + s
            
    def isPalindrome(self, pre_string, s):
        # so, what am i doing here?
        # what's the total length?
        
        total_len = len(pre_string) + len(s)
        
        # if even, what's the mid point?
        # total_len // 2
        # (total_len // 2) - 1
        
        # if odd, what's the mid point?
        # total_len // 2
        
        # with mid point, i can expand outwards.
        # in both cases, i'd do `total_len//2`
        
        right = total_len // 2
        
        is_even = total_len % 2 == 0
        if is_even:
            left = right - 1
        else:
            left = right
            
        # now we expand..
        while left >= 0 and right < total_len:
            valueLeft = self.getValue(left, pre_string, s)
            valueRight = self.getValue(right, pre_string, s)
            
            if valueLeft != valueRight:
                return False
            
            left -= 1
            right += 1
            
        return True
    
    def getValue(self, idx, pre_string, s):
        # the question is where is the index stored?
        # `pre_string` or `s`
        
        # well, how do i know, if idx is < len(pre_string)
        # it's in pre-string.
        
        # if it's >= len(pre_string)
        # it's in `s`
        
        psLen = len(pre_string)
        if idx < psLen:
            return pre_string[idx]
        
        return s[
            idx - psLen
        ]
        
arr = [
    "abcd",
    "aacecaaa",
]
foo = arr[-1]
sol = Solution()
res = sol.shortestPalindrome(foo)
print(res)
        
        
        

