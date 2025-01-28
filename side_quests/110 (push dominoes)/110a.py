# https://leetcode.com/problems/push-dominoes/description/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        pass
        # find every RL pair
        # define start and end indices
        # and move inward
        # for each index at start, change it to R
        # for each index at end, change it to L
        # unless start and end are equal in which case, do nothing
        
        L, R = 'L', 'R'
        forward, backward = 0, 0
        
        dim = len(dominoes)
        while backward < dim:
            pass
            ch = dominoes[backward]
            if ch == L:
                pass
                self.fallout(forward, backward)
                
    # TODO redefine variables, what happens when you deal with 
    # (None, L), (R, L) and (R, None)?
    def fallout(self, forward, backward, dominoes):
        L, R = 'L', 'R'
