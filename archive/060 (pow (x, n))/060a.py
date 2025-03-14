# https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, og_num: float, exponent: int) -> float:
        num = og_num
        places = abs(exponent)

        res = self.explore(num, places)
        if exponent < 0:
            res = 1/res
        return res

    def explore(self, num, places):
        if places == 0:
            return 1
        elif places == 1:
            return num
        elif num == 0:
            return 0

        pair = num * num
        num_of_pairings, rem = divmod(places, 2)


        return self.explore(pair, num_of_pairings) * (num if rem else 1)



    
arr = [
    [2.1, 3],
    [2, 10],
    [0.00001, 2147483647],
    [2, 5],
    [2, 2],
    [-2, -3],
    [0, 30],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.myPow(foo, bar)
print(res)
