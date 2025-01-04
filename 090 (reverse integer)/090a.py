# https://leetcode.com/problems/reverse-integer/description/

# TODO https://neetcode.io/solutions/reverse-integer
class Solution:
    def reverse(self, x: int) -> int:
        pass
        # declare a variable `is_neg`, it checks if `x` is a negative number
        # x = abs(x)
        # create an array, `arr`
        # using a while loop where you mod `x` by 10 and get the remainder
        # store the reverse of `x` in the `arr`
        
        if x == 0: 
            return 0

        is_neg = x < 0
        
        x = abs(x)
        arr = []
        
        while x:
            x, digit = divmod(x, 10)
            
            if digit == 0 and not arr:
                continue
            arr.append(digit)
            
        limit = list(str(2 ** 31))
        
        # ensure the reversed number is not greater than limit
        
        if len(limit) == len(arr):
            dim = len(limit)
            for idx in range(dim):
                a, b = limit[idx], arr[idx]
                a, b = int(a), int(b)
                
                if idx == dim - 1 and not is_neg:
                    a -= 1
                
                if a > b:
                    break
                if a < b:
                    return 0
            

        res = int(''.join(str(ch) for ch in arr))
        return -res if is_neg else res
        
        
        
arr = [
    -123,
    120,
]
foo = arr[-1]
sol = Solution()
res = sol.reverse(foo)
print(res)
