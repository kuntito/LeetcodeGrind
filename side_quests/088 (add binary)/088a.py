# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pass
        # create an array that's the length of the longest argument + 1
        dim = max(len(a), len(b)) + 1
        arr = [0 for _ in range(dim)]
        
        # create two pointers, idxOne and idxTwo
        # that start at the end of each string
        
        idxOne = len(a) - 1
        idxTwo = len(b) - 1
        
        # while both pointers are valid, do a binary addition on their values
        # and insert into `arr`
        # the longest index + 1 determines the insertion point
        
        while idxOne >= 0 and idxTwo >= 0:
            valOne = int(a[idxOne])
            valTwo = int(b[idxTwo])
            
            zum = valOne + valTwo
            
            insertIdx = max(idxOne, idxTwo) + 1
            arr[insertIdx] += zum
            
            quo, rem = divmod(arr[insertIdx], 2)
            arr[insertIdx] = rem
            arr[insertIdx-1] = quo
            
            
            idxOne -= 1
            idxTwo -= 1
            
            
        self.if_valid_continue_iter(idxOne, a, arr)
        self.if_valid_continue_iter(idxTwo, b, arr)
        
        if arr[0] == 0:
            arr = arr[1:]
        
        return ''.join(str(i) for i in arr)
            
    def if_valid_continue_iter(self, idx, chars, arr):
        while idx >= 0:
            insertIdx = idx + 1
            val = int(chars[idx])
            arr[insertIdx] += val
            
            quo, rem = divmod(arr[insertIdx], 2)
            arr[insertIdx] = rem
            arr[insertIdx-1] = quo
            
            idx -= 1
            
            
            
        
arr = [
    ["11", "1"],
    ["1010", "1011"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.addBinary(foo, bar)
print(res)
