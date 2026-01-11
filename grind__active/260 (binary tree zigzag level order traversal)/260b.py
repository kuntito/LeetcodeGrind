# https://leetcode.com/problems/zigzag-conversion/

# zig zag pattern
# what does this mean?
# there's three horizontal lines

# the first character of string, `char1`
# is the first character on the first line

# `char2`, the second character of the string is the first character on the second line.

# similarly, `char3` is the first on the third line

# if you notice, with each character, we moved downwards, char1 = first line, char2 = second line, char3 = third line.

# since we only have three lines, we can't go any lower and now must go up
# 
# this way, the next char, `char4` becomes the second character on the second line

# seems to me like i can iterate through the string with a counter, to know what line i'm on

# i only have three horizontal lines, so i can have an array for each line
# appending each character as i go along.

# but how do i know if i'm going downwards or upwards

# how about a circular -
# i'm thinking of using a pointer that's always modded by `3`

# initially, the -
# the pointer can be the index % 3

# the first three indices would be 0, 1, 2
# and the characters here can be mapped to 
# the arrays representing the first, second and third lines

# the next indices would be 3, 4, 5
# but when you mod them, you'd be back to 0, 1, 2

# nah, this doesn't work.

# your pattern should look like 0 1 2 1 0..

# almost like your pointer has an increment
# initially, it's +1, with every index, you add `1`

# once you hit the wall, `2`
# you flip the increment, it becomes `-1`
# 2, 1, 0
# once, you hit zero, you flip again

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        incr = -1
        line = 0
        
        all_lines = {i:list() for i in range(numRows)}
        
        for ch in s:
            all_lines[line].append(ch)
            
            if line == 0 or line == numRows-1:
                incr = -1 * incr
            
            line += incr
            
        res = []
        for line, chars in all_lines.items():
            
            res.extend(chars)
            
        return "".join(res) 


arr = [
    ["PAYPALISHIRING", 3],
    ["AB", 1],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.convert(foo, bar)
print(res)