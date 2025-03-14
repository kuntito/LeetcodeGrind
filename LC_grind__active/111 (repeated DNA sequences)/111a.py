# https://leetcode.com/problems/repeated-dna-sequences/description/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        pass
        dim = len(s)
        counter = {}
        # sliding window of size 10
        # get a slice of the string and put it in a hashmap
        for idx in range(9, dim):
            start, end = idx - 9, idx + 1
            sequence = s[start: end]
            
            counter[sequence] = counter.get(sequence, 0) + 1
            
        
        # return the number of sequences with more than 1 freq
        return [seq for seq, count in counter.items() if count > 1]
    
arr = [
    "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
    "AAAAAAAAAAA"
    "AAAAAAAAAAAAA",
]
foo = arr[-1]
sol = Solution()
res = sol.findRepeatedDnaSequences(foo)
print(res)