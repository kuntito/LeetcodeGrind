# https://leetcode.com/problems/add-digits/description/

# TODO find explainer
class Solution:
    def addDigits(self, num: int) -> int:
        pass
        # convert the number to an array of it's digits
        
        num_arr = [int(dch) for dch in str(num)]
        total = sum(num_arr)
        
        if total < 10:
            return total
        else:
            return self.addDigits(total)

    
    
arr = [
    0,
    38,
]
foo = arr[-1]
sol = Solution()
res = sol.addDigits(foo)
print(res)
            
