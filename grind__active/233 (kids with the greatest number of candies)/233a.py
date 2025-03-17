class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        pass
        # determine the largest candy throughout the array
        # iterate through the array with idx
        
        # increment the child's candy by `extraCandies`
        # if the new amount is greater than or equal to the largest initial candy
        
        # set candies[idx] = True else False
        
        greatest = max(candies)
        
        for idx, candy in enumerate(candies):
            newCandy = candy + extraCandies
            
            if newCandy >= greatest:
                candies[idx] = True
            else:
                candies[idx] = False
                
        return candies
    
arr = [
    [[2, 3, 5, 1, 3], 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.kidsWithCandies(foo, bar)
print(res)