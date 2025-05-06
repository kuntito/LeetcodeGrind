# https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # to make sure i understand, can i repeat what i think the question is asking
        
        # we're given a grid of letters
        # ordered in a zig zag pattern
        
        # and we want to print the correct order ot the characters in the string
        
        # the first thing is to understand the zig zag order
        # staring at the sample example
        
        # we're given "PAYPALISHIRING"
        # and the grid:
        # P   A   H   N
        # A P L S I I G
        # Y   I   R
        
        # if we pay attention, we can see the order of the characters is such that...
        
        # i believe i have misunderstood the question.
        # we aren't given a grid
        
        # TODO `before you go on a tangent, understand the nature of the arguments`
        
        # to make sure i understand the question, i'd ask some clarifying questions
        # we're given a string that reads in a zig zag pattern
        # this pattern as we're shown in the example is dependent on the number of rows
        
        # consider the string "PAYPALISHIRING" and numRows = 3
        
        # to determine the grid, we would pick the first `n` characters
        # which serve as the first column, moving downwards
        
        # once we hit rock bottom, we take `n - 2` characters
        # this represents the climb and each character we meet on the climb
        # is it's own column
        # once we've exhausted the climb we would have now reached the top
        # we repeat the process till we run out of characters
        
        # P   A   H   N
        # A P L S I I G
        # Y   I   R
        
        # using this grid, we can then concatenate the characters on every row to convert the message
        
        # however, do we need to create a grid
        # for every row where i add a character
        # i'd create a list for it's elements
        # and add elements as i go along
        # and once, i'm done, i can concatenate the contents of each row and return the final message
        
        # might have to create a grid in the end
        grid = [[] for _ in range(numRows)]
        
        climbing = False
        idx = 0
        dim = len(s)
        
        rowIdx = 0
        while idx < dim:
            # we start at the first row and go down
            # for each row what do we do
            # we 
            
            rowIdx += 1