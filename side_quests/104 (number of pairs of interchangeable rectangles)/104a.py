# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/description/

import math
class Solution:
    def __init__(self):
        pass
        self.fact_memo = {}
    
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        pass
    
        # create a hashmap that stores the ratio of each rectangle
        # loop through the hashmap and determine how many ways you can select 2
        # rectangles from the number of rectangles per ratio
        
        # sum up the results of the selection and return it  
        
        all_ratios = {}
        for width, height in rectangles:
            ratio = width/height
            all_ratios[ratio] = all_ratios.get(ratio, 0) + 1
            
        res = 0
        for count in all_ratios.values():
            if count > 1:
                res += math.comb(count, 2)
                
        return int(res)
            
        
    # TODO is it the memo that makes it slow?
    # TODO while loop instead of recursion?
    def combination(self, n, r):
        pass
        n_fact = self.factorial(n)
        r_fact = self.factorial(r)
        n_r_fact = self.factorial(n - r)
        
        return n_fact / (r_fact * n_r_fact)
    
    def factorial(self, n):
        if n <= 1:
            return 1
        
        res = n * self.factorial(n-1)
        self.fact_memo[n] = res
        return self.fact_memo[n]
    
arr = [
    [[4,5],[7,8]],
    [[4,8],[3,6],[10,20],[15,30]],
]
foo = arr[-1]
sol = Solution()
res = sol.interchangeableRectangles(foo)
print(res)