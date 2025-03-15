# https://leetcode.com/problems/add-to-array-form-of-integer/description/

# https://neetcode.io/solutions/add-to-array-form-of-integer
# 07:33
class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        pass
        # convert the array form to a number
        n = self.get_num(num)
        
        # add it to k
        combined = n + k
        # convert the result into a number array
        res = self.convert_to_num_arr(combined)
        return res
        
        
    def convert_to_num_arr(self, combined):
        if combined == 0:
            return [0]
        
        res = []
        while combined:
            combined, dig = divmod(combined, 10)
            res.append(dig)
            
        return res[::-1]
                
        
    def get_num(self, num_arr):
        pass
        res = 0
        
        dim = len(num_arr)
        for idx in range(dim-1, -1, -1):
            val = num_arr[idx]
            exp = dim - 1 - idx
            
            val = val * 10 ** exp
            
            res += val
        return res
    
arr = [
    [[1, 2, 0, 0], 34],
    [[2, 7, 4], 181],
    [[0], 0],
]
foo, bar = arr[-1]

sol = Solution()
res = sol.addToArrayForm(foo, bar)
print(res)
