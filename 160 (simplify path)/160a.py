# https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        pass
        # separate into tokens
        # the end of each token is defined by the a character
        # that's not a forward slash and the next ch is either out of bounds
        # or a forward slash


        
        dim = len(path)
        
        
        fslash = r'/'
        token = []
        
        for idx, ch in enumerate(path):
            pass