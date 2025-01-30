# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:

        return self.explore(0, rowIndex, [])
    
    def explore(self, ri, targetRi, arr):
        if ri > targetRi:
            return arr
        
        if ri < 2:
            arr.append(1)
        else:
            temp = [1]
            for idx in range(1, len(arr)):
                foo = arr[idx] + arr[idx - 1]
                temp.append(foo)
            temp.append(1)
            arr = temp

        return self.explore(ri + 1, targetRi, arr)
        

arr = [
    0,
    3,
    4,
]
foo = arr[-1]
sol = Solution()
res = sol.getRow(foo)

print(res)