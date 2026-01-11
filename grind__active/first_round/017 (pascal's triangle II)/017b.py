# https://leetcode.com/problems/pascals-triangle-ii/description/

# TODO https://neetcode.io/solutions/pascals-triangle-ii
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        pass
        res = [1]
        
        dim = rowIndex
        for i in range(dim):
            pass
            temp = [0 for _ in range(len(res) + 1)]
            for j, val in enumerate(res):
                temp[j] += val
                temp[j + 1] += val
                
            res = temp
        
        return res


arr = [
    0,
    4,
    3,
]
foo = arr[-1]
sol = Solution()
res = sol.getRow(foo)

print(res)