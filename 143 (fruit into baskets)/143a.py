# https://leetcode.com/problems/fruit-into-baskets/description/

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        pass
        # find the longest subarray with two distinct elements
        # two pointers, representing a window
        # keep track of the number of unique characters in the window
        # once you encounter a new unique character, update the curr window len
        # move the left pointer until the number of unique characters in the window is less than 2
        
        dim = len(fruits)
        left = 0
        
        res = None
        basket = {}
        for right in range(dim):
            pass
            ft = fruits[right]
            if ft not in basket and len(basket) == 2:
                dist = (right - left) + 1
                if res is None:
                    res = dist
                else:
                    res = max(res, dist)
                    
                while len(basket) == 2:
                    leftFruit = fruits[left]
                    basket[leftFruit] -= 1
                    if basket[leftFruit] == 0:
                        del basket[leftFruit]
                    left += 1
            
            
            basket[ft] = basket.get(ft, 0) + 1
        
        dist = (len(fruits) - left) + 1
        if res is None:
            res = dist
        else:
            res = max(dist, res)
        
        return res
    
arr = [
    [1,2,1],
    [1,2,3,2,2],
]
foo = arr[-1]
sol = Solution()
res = sol.totalFruit(foo)
print(res)
    
    