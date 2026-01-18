# https://leetcode.com/problems/excel-sheet-column-title/
from string import ascii_uppercase

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        arr = []
        self.explore(columnNumber, arr)
        return ''.join(arr[::-1])
    
    def explore(self, num, arr):
        twosix = 26
        # if the number is <= 26, map it to a char and store it
        if num <= twosix:
            arr.append(self.map_char(num))
        else:
            quo, rem = divmod(num, twosix)
            
            # it means the number is evenly divided by 26
            if rem == 0:
                arr.append(self.map_char(twosix))
                quo -= 1
            else:
                arr.append(self.map_char(rem))
                
            self.explore(quo, arr)
    
            

    def map_char(self, number):
        if number < 1 or number > 26:
            raise Exception(f'invalid number {number}')
        
        return ascii_uppercase[number-1]
    
arr = [
    52,
]
foo = arr[-1]
sol = Solution()
res = sol.convertToTitle(foo)
print(res)