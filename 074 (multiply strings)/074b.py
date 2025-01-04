# https://leetcode.com/problems/multiply-strings/description/

# https://neetcode.io/solutions/multiply-strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        zero = '0'
        if num1 == zero or num2 == zero:
            return zero
        
        # determine the long and short digits
        # for each digit in the shorter one, 
        # multiply every digit in the longer one
        # place the result in `arr`
        
        maxDigitCount = len(num1) + len(num2)
        slots = [0 for _ in range(maxDigitCount)]
        
        short, lng = self.get_short_and_long(num1, num2)
        
        incr = len(short)
        for sh_idx in range(len(short)-1, -1, -1):
            sh_dig = int(short[sh_idx])
            
            for lng_idx in range(len(lng)-1, -1, -1):
                lng_dig = int(lng[lng_idx])
                
                mult = sh_dig * lng_dig
                
                place_idx = lng_idx + incr
                self.place(mult, place_idx, slots)
            incr -= 1

        res = ''
        idx = 0
        while idx < len(slots) and slots[idx] == 0:
            idx += 1
                
        return ''.join(str(ch) for ch in slots[idx:])
            
            
    def place(self, mult, idx, slots):
        while mult:    
            dig = mult % 10
            
            new_val = slots[idx] + dig
            quo, rem = divmod(new_val, 10)
            slots[idx] = rem
            
            if quo:
                self.place(quo, idx-1, slots)
                
            mult //= 10
            idx -= 1

            
        
    def get_short_and_long(self, a, b):
        return (a, b) if len(a) < len(b) else (b, a)



arr = [
    ["5", "5"],
    ["123", "456"],
    # ["12", "5"],
    ["999", "999"],
    ["29", "22"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.multiply(foo, bar)
print(res)

