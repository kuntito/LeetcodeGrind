# https://leetcode.com/problems/license-key-formatting/description/

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # convert the string to an array of chars
        # exclude the hyphen when creating the array
        chars = [ch.upper() if ch.isalpha() else ch for ch in s if ch != '-']
        chars = ''.join(str(ch) for ch in chars)
        # at this point, we know how many non-hyphen characters we have
        validCount = len(chars)
        # use divmod to determine the chunk sizes
        
        firstChunkLen = validCount % k
        
        
        # the remainder is the size of the first chunk and the other chunks are of size k
        
        res = []
        if firstChunkLen: res.append(chars[:firstChunkLen])
        dim = len(chars)
        
        for i in range(firstChunkLen, dim, k):
           res.append(chars[i:i+k])
        
        
        return '-'.join(res)