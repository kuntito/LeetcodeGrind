# https://leetcode.com/problems/pascals-triangle/description/



class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(1, numRows + 1):
            temp = []
            if i > 1:
                last = res[-1]
                temp.append(1)
                for idx in range(len(last)-1):
                    temp.append(last[idx] + last[idx+1])

            temp.append(1)
            res.append(temp)

        return res
    
arr = [
    5,
]
foo = arr[-1]
sol = Solution()
res = sol.generate(foo)

for row in res:
    print(row)