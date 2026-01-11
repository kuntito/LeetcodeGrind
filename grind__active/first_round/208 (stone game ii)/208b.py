# https://leetcode.com/problems/stone-game-ii/description/


# TODO write code based on reasoning
class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        pass
        # at each position, we want to know how many picks are possible
        # and what the best option is
        
        # consider, the following examples
        # assume you can pick all the items
        # for [4]
        # you best option is the only option
        
        # for [4, 4]
        # your best option is picking both of them
        
        # at each point, we don't know the best option for the current user
        # so we explore all their options and track the best one
        
        # for [9, 4, 4], assuming i can only pick `2`
        # my best option is [9, 4]
        
        # if i know the best option for a particular user,
        # how does that influence the next user's options
        
        # the idea is, i pick `one`
        # if i pick one, the array becomes arr[1:]
        # what's the best someone can pick in `arr[1:]` with `2M` constraints, where M = 1
        
        # i find out and store the results to avoid repeated work
        # i pick `two`, the array becomes `arr[2:]`
        # what's the best someone can pick in `arr[2:]` with `2M` constraints, where M=2
    
        # since i'm tracking all my options
        # i can return the answer in the first loop
        # the work is done in the recursive functions
        
        # the base case would be when you can pick all the piles
  
            
arr = [
    [2,7,9,4,4],
]
foo = arr[-1]
sol = Solution()
res = sol.stoneGameII(foo)
print(res)