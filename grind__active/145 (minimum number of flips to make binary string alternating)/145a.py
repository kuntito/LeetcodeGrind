# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/

class Solution:
    def minFlips(self, s: str) -> int:
        pass
    
        # the string can either be a series of 01 or 10
        # declare two pointers, `uno` and `dos`
        # iterate through `s` such and keep count the number of changes needed to convert the string to a series of `01` and store in `uno`
        # also keep track of the number of changes if would require to convert the string to a series of `10`
        # return the lesser one
        
        left_arr = self.get_left(s)
        right_arr = self.get_left(s)
        
        dim = len(s)
        res = None
        for idx in range(dim):
            u1, d1 = left_arr[idx]
            u2, d2 = right_arr[idx + 1] if idx + 1 < dim else (0, 0)
            
            min_type = min(
                (u1 + u2),
                (d1 + d2)
            )
            if res is None:
                res = min_type
            else:
                res = min(res, min_type)
            
        return res
            
        
    def get_left(self, chars):
        left_arr = []
        
        uno = 0
        for idx, ch in enumerate(chars):
            pass
            if idx % 2:
                if ch == '0':
                    uno += 1
            else:
                if ch == '1':
                    uno += 1
                    
            dos = (idx + 1) - uno
            left_arr.append(
                (uno, dos)
            )

        return left_arr
    
    def get_right_arr(self, chars):
        dim = len(chars)
        uno = 0
        right_arr = []
        
        for idx in range(dim-1, -1, -1):
            ch = chars[idx]
            if idx % 2:
                if ch == '0':
                    uno += 1
            else:
                if ch == '1':
                    uno += 1
                    
            dos = dim - idx - uno
            right_arr.append((uno, dos))
            
        return right_arr

arr = [
    "1110",
    "010",
    "111000",
]
foo = arr[-1]
sol = Solution()
res = sol.minFlips(foo)
print(res)