# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/

# TODO https://neetcode.io/solutions/unique-length-3-palindromic-subsequences
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pass
        # a 3-char palindrome is exists if you have two of the same chars
        # separated by at least one character
        # if you explore all the different ways two same chars can exist
        # and count the number of unique chars between them
        
        # create a map for each character, store it's earliest index and it's latest index
        # run through the structure
        # determine the number of unique elements between each char set
        # add it up in res, game over
        
        charmap = {}
        for idx, ch in enumerate(s):
            if ch in charmap:
                charmap[ch][1] = idx
            else:
                charmap[ch] = [idx, None]
              
        res = 0  
        for pair in charmap.values():
            left, right = pair
            if isinstance(left, int) and isinstance(right, int) and (left + 1 <= right):
                betweens = s[left + 1: right]
                res += len(set(betweens))
        return res
                
            
        
        
        
            
arr = [
    "adc",
    "bbcbaba",
    "aabca",
    "tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp"
]
foo = arr[-1]
sol = Solution()
res = sol.countPalindromicSubsequence(foo)
print(res)