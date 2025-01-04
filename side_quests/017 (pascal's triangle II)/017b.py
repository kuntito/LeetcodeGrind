# https://leetcode.com/problems/pascals-triangle-ii/description/

# TODO https://neetcode.io/solutions/pascals-triangle-ii
# 04:37
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        
        # create an array, `arr` of size `rowIndex+1`
        # initialize the first two positions with `1`s, others should be `None`
        # `arr[0] = 1`
        # `arr[1] = 1`
        # for i in range(2, rowIndex + 1)
        # loop through the values in arr, whose values are not `None`
        # FIXME you might need two arrays of size `rowIndex + 1`

arr = [
    0,
    3,
    4,
]
foo = arr[-1]
sol = Solution()
res = sol.getRow(foo)

print(res)