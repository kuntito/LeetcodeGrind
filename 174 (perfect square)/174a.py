# https://leetcode.com/problems/perfect-squares/description/

class Solution:
    def numSquares(self, n: int) -> int:
        # it's similar to the coin change problem
        # in this case the coins are the perfect squares
        # you want to find the least amount of perfect squares
        # that make up the `n`

        # to find the viable perfect squares
        # run a while loop from `1 to n (inclusive)`
        # append every `i` such that `i**2 <= n`
        # if `i**2 > n`, stop the loop

        coins = []
        for i in range(1, n + 1):
            pf_sq = i ** 2
            if pf_sq > n:
                break
            coins.append(pf_sq)

        # then it becomes a recursive process
        # where you take away the highest value coin from `n`
        # if you hit zero, happy days

        prevRow = [None for _ in range(n)]

        # coins = [4, 9]
        for c in coins:
            curRow = [None for _ in range(n)]
            for idx in range(n):
                am = idx + 1
                
                valueAbove = prevRow[idx]
                valueHere = None
                
                diff = am - c
                if diff == 0:
                    valueHere = 1
                elif diff > 0 and curRow[diff-1]:
                    valueHere = 1 + curRow[diff-1]
                    
                if valueAbove and valueHere:
                    curRow[idx] = min(valueAbove, valueHere)
                elif valueAbove:
                    curRow[idx] = valueAbove
                else:
                    curRow[idx] = valueHere
                    
            prevRow = curRow
       
        # print(prevRow)
        return prevRow[-1]
    
arr = [
    12,
    5,
    4,
    13,
]
foo = arr[-1]
sol = Solution()
res = sol.numSquares(foo)
print(res)