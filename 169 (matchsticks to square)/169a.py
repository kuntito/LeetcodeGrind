# https://leetcode.com/problems/matchsticks-to-square/description/

class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        pass
        # is the sum of matchsticks divisible by `4`
        total = sum(matchsticks)
        if total % 4:
            return False
        
        each_len = total // 4
        
        # create a hashmap for the matchsticks
        counter = {}
        # sort the match sticks
        matchsticks.sort()
        for m in matchsticks:
            counter[m] = counter.get(m, 0) + 1
        
        
        # starting from the largest match stick
        while matchsticks:
            # if the largest match stick not in hashmap
            # return False
            largest = matchsticks.pop()
            if largest not in counter:
                return False
            counter[largest] -= 1

            if largest == each_len:
                continue
            
            complement = each_len - largest
            if complement < 0:
                return False
            
            # search the hashmap for it's complement
        
            # if absent, run a loop from (complement - 1, -1, -1)
            # if the complement doesn't exist, return False
            # if it does, update the hashmap removing any exhausted compliments
        
            for comp in range(complement, -1, -1):
                while comp in counter and complement > 0:
                    complement -= comp
                    counter[comp] -= 1
                    
                    if counter[comp] == 0:
                        del counter[comp]
                        
                if complement == 0:
                    break
        
        
        return True
    
arr = [
    [1,1,2,2,2],
]
foo = arr[-1]
sol = Solution()
res = sol.makesquare(foo)
print(res)