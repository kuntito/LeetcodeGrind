# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/

class Solution:
    def minOperations(self, s: str) -> int:
        zero_count = 0
        patOne_count = 0

        # the question, is it cheaper if the string starts with a `0` or starts with a `1`?
        
        # if it starts with `0`, the pattern should be `010101...`
        # count how many times the current string deviates from this pattern
        
        # if it starts with `1`, the pattern should be `101010..`
        # count how many times the current string deviates from this pattern
        
        # return the smaller one
        dim = len(s)

        patOne_count = 0
        patTwo_count = 0
        for idx in range(0, dim, 2):
            pass
            
            ch = s[idx]
            nextCh = s[idx + 1] if idx + 1 < dim else None
            
            # 01 pattern
            if ch != '0':
                patOne_count += 1
            if nextCh and nextCh != '1':
                patOne_count += 1
                
            # 10 pattern
            if ch != '1':
                patTwo_count += 1
            if nextCh and nextCh != '0':
                patTwo_count += 1
                
        
        return min(patOne_count, patTwo_count)
            
