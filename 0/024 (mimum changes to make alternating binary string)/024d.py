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

        count = 0
        for idx, ch in enumerate(s):
            if idx % 2:
                count += 1 if ch == '0' else 0
            else:
                count += 1 if ch == '1' else 0
        
        
        return min(count, dim - count)
            
