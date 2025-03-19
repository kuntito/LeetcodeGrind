# https://leetcode.com/problems/number-complement/description/

class Solution:
    def findComplement(self, num: int) -> int:
        pass
        get_binary = lambda x: list(bin(x)[2:])
        get_num_from_bin = lambda x: int(x, 2)
        
        
        binary_str = get_binary(num)
        
        for idx, ch in enumerate(binary_str):
            binary_str[idx] = '1' if ch == '0' else '0'


        # remove leading zeros if any
        idx = 0
        dim = len(binary_str)
        # while the string has at least two chars and the current char is zero
        while idx < dim - 1 and binary_str[idx] == '0':
            idx += 1
            
        binary_str = binary_str[idx:]
            
        return get_num_from_bin("".join(binary_str))
        
arr = [
    5,
    1,
]    
foo = arr[-1]
sol = Solution()
res = sol.findComplement(foo)
    

print(res)