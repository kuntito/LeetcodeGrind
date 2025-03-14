# https://leetcode.com/problems/sequential-digits/description/

# TODO it works, but write it simpler
class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        pass
        # turn `high` into an array of it's digits
        # create `arr` of size `len(high)`
        
        
        high_arr = [int(d) for d in str(high)]
        
        
        low_arr = [int(d) for d in str(low)]
        arr = [-1 for _ in low_arr]
        dim = len(arr)
        
        res = []
        seen = set()
        while len(arr) <= len(high_arr) or arr[0] <= high_arr[0]:
            pass
            for idx in range(dim):
                if idx == 0:
                    arr[idx] += 1
                else:
                    arr[idx] = arr[idx - 1] + 1
                    
            candidate = self.convert_to_int(arr)
            # print(candidate)
            if candidate >= low and candidate <= high:
                if candidate not in seen:
                    res.append(candidate)
                    seen.add(candidate)
                
            if arr[-1] == 9:
                arr.append(0)
                arr[0] = -1
                dim = len(arr)
                
            
        return res
    
    def convert_to_int(self, arr):
        dim = len(arr)
        
        res = 0
        unit = dim - 1
        for dig in arr:
            dig = dig * (10 ** unit)
            res += dig
            unit -= 1
            
        return res
        
        
arr = [
    [100, 300],
    [1000, 13000]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.sequentialDigits(foo, bar)
print(res)
