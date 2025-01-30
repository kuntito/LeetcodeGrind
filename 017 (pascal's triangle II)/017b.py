# https://leetcode.com/problems/pascals-triangle-ii/description/

# TODO https://neetcode.io/solutions/pascals-triangle-ii
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        pass
        # create an array of size `rowIndex + 1`
        dim = rowIndex + 1
        arr = [1 for _ in range(dim)]
        
        for i in range(2, dim):
            clone = arr[::]
            for j in range(i, dim-1):
                pass
                clone[j] = clone[j] + clone[j-1]
                
        
        return arr

arr = [
    0,
    3,
    4,
]
foo = arr[-1]
sol = Solution()
res = sol.getRow(foo)

print(res)