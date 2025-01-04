# https://leetcode.com/problems/maximum-odd-binary-number/description/

# TODO https://neetcode.io/solutions/maximum-odd-binary-number
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        pass
        # count the number of 1s in `s`, `ones_count`
        # create an array of size len(s), `arr`
        # `arr[-1] = '1'`
        # `ones_count -= 1`
        
        # loop through `arr` with index
        # while `ones_count > 0`
        # place `1` at each index till you run out of ones
        
        ones_count = sum(1 for ch in s if ch == '1')
        
        dim = len(s)
        arr = ['0' for _ in range(dim)]
        arr[-1] = '1'
        ones_count -= 1
        
        
        for idx in range(dim):
            if ones_count == 0: break
            
            arr[idx] = '1'
            
            ones_count -= 1
            
        return ''.join(arr)

arr = [
    "0101",
    "010",
]
foo = arr[-1]
sol = Solution()
res = sol.maximumOddBinaryNumber(foo)
print(res)