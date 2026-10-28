class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        idx = 1
        binary = list(binary)
        
        dim = len(binary)
        
        zeroCount = 0
        while idx < dim:
            uno = binary[idx - 1]
            dos = binary[idx]
            
            if uno == '0' and dos == '0':
                binary[idx - 1] = '1'
                
            if uno == '1' and dos == '0' and zeroCount:
                binary[idx - 1] = '0'
                binary[idx] = '1'
                
                idx -= 1
                continue
        
            if uno == '0':
                zeroCount += 1
                
            idx += 1
            
        return ''.join(binary)

arr = [
    "000110",
]
foo = arr[-1]
sol = Solution()
res = sol.maximumBinaryString(foo)

print(res)

                
            