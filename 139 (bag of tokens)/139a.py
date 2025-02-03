# https://leetcode.com/problems/bag-of-tokens/description/

class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        pass
        # sort the tokens
        # two pointers, left and right
        
        # ideally, you want to play face up from the left
        # if that's not possible play face down from the right
        # if that isn't possible, end the game
        
        # track maxCount through each play through
        
        tokens.sort()
        
        dim = len(tokens)
        left, right = 0, dim - 1
        
        score = 0
        maxScore = 0
        
        while left <= right: 
            leftKen = tokens[left]
            if power >= leftKen:
                power -= leftKen
                score += 1
                
                maxScore = max(score, maxScore)
                left += 1
            elif score:
                power += tokens[right]
                score -= 1
                
                right -= 1
            else:
                break
            
        return maxScore
    
arr = [
    [[100], 50],
    [[200,100], 150],
    [[100,200,300,400], 200],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.bagOfTokensScore(foo, bar)

print(res)