# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/description/

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

from typing import List

# i want to implement a function, `read4`, that returns an integer.
# the function takes two arguments, a string array, `buf` and an integer, `n`

# i'm given a file and i can only read that file using a method, `read4`.

# they want me to implement a method, `read` to read `n` characters from the file.
# let's break this down. the file exists and i can only access it using `read4` method.

# now, they want me to implement my own read function, `read_n`
# this reads `n` characters from the file. since, the only way i can access
# the file is by using `read4` then my `read_n` has to be a mapper around `read4`

# one more thing, whenever `read4` is called, it reads four consecutive characters and writes said consecutive characters into an array, `buf4`

# `read4` also has a return type, int.
# this refers to the actual amount of characters read from the file.
# if the file contains "abc", `read4` can only read 3 characters, hence, returns 3.

# 
class Solution:
    def read(self, buf: List[str], n: int) -> int:
        prevSize = 0
        charsRead = 0
        
        firstTime = True
        
        # the question is odd. the given examples have a return type of integer array
        # the function in the question has return type integer.
        
        # from what i can gather, i should call `read4` until i've read `n` items
        # from the file
        # they want me to return how many characters i read?
        # 
        # but wouldn't that be `n`?
        # i just tried to return `n` and failed the example test case
        
        # turns out it actually expects an array of integers
        while firstTime or len(buf) > prevSize:
            firstTime = False
            
            # read4(buf)
            
            
        return charsRead