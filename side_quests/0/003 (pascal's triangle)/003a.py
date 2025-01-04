# https://leetcode.com/problems/pascals-triangle/description/


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        return self.explore(numRows, 1, [])
    
    def explore(self, numRows, currRow, res):
        if currRow > numRows:
            return res
        
        if currRow == 1:
            res.append([1])
        elif currRow == 2:
            res.append([1, 1])
        else:
            last_row = res[-1]
            new_row = [1]

            # the `-1` prevents the out of bounds error
            # in `idx + 1`
            foo = len(last_row)-1
            for idx in range(foo):
                new_row.append(
                    last_row[idx] + last_row[idx + 1]
                )
            new_row.append(1)

            res.append(new_row)

        return self.explore(numRows, currRow+1, res)
    

arr = [
    5,
]
foo = arr[-1]
sol = Solution()
res = sol.generate(foo)

for row in res:
    print(row)