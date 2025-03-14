# https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        pass
        # create a result array, `arr` 
        # create a variable `starCount`
        
        # iterate through `s` in reverse
        # increment starCount
        # append any non star characters to `arr` if `starCount == 0`
        # else skip
        
        # reverse `res` and return
        
        
        res = []
        starCount = 0
        dim = len(s)
        
        for idx in range(dim-1, -1, -1):
            ch = s[idx]
            if ch == "*":
                starCount += 1
            elif starCount == 0:
                res.append(ch)
            else:
                starCount -= 1

                
        return "".join(res[::-1])
    
    
arr = [
    "leet**cod*e",
    "erase*****",
]
foo = arr[-1]
sol = Solution()
res = sol.removeStars(foo)
print(res)