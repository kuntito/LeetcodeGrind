# https://leetcode.com/problems/roman-to-integer/description/

# TODO https://neetcode.io/solutions/roman-to-integer
# 07:21 deep solution
class Solution:
    def romanToInt(self, s: str) -> int:
        pass
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        # using a while loop, iterate through each char in `s`
        idx = 0
        res = 0
        while idx < len(s):
            pass
            # if the value at idx + 1  is greater than the current value
            # take them both your next integer is 
            ch = s[idx]
            val = roman_to_int[ch]
            
            if idx + 1 < len(s):
                nextCh = s[idx + 1]
                nextChVal = roman_to_int[nextCh]
                if nextChVal > val:
                    val = nextChVal - val
                    idx += 1
                    
            res += val
            idx += 1
            
        return res
    
arr = [
    "III",
    "LVIII",
    "MCMXCIV",
]
foo = arr[-1]
sol = Solution()
res = sol.romanToInt(foo)
print(res)