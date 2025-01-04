# https://leetcode.com/problems/powx-n/description/


class Solution:
    def myPow(self, og_num: float, exponent: int) -> float:
        res = self.explore(og_num, abs(exponent))
        return res if exponent >= 0 else 1/res


    def explore(self, num, exponent):
        if num == 0:
            return 0
        if exponent == 0:
            return 1
        
        res = self.explore(num, exponent//2)
        square = res * res
        return num * square if exponent % 2 else square
    
"""
consider these two code blocks, block A class Solution:
    def myPow(self, og_num: float, exponent: int) -> float:
        res = self.explore(og_num, abs(exponent))
        return res if exponent >= 0 else 1/res


    def explore(self, num, exponent):
        if num == 0:
            return 0
        if exponent == 0:
            return 1
        
        res = self.explore(num, exponent//2)
        square = res * res
        return num * square if exponent % 2 else square and block B, class Solution:
    def myPow(self, og_num: float, exponent: int) -> float:
        res = self.explore(og_num, abs(exponent))
        return res if exponent >= 0 else 1/res


    def explore(self, num, exponent):
        if num == 0:
            return 0
        if exponent == 0:
            return 1
        
        res = self.explore(num, exponent//2)
        square = res ** 2
        return num * square if exponent % 2 else square


the two are logically identical but the line square = res ** 2 causes an OverflowError: (34, 'Numerical result out of range') for a test case where the initial exponent is -2147483648

why? is res * res not the same as res ** 2?
"""



    
arr = [
    [2.1, 3],
    [2, 10],
    [0.00001, 2147483647],
    [2, 5],
    [-2, -3],
    [0, 30],
    [2, 2],
    [2, -2147483648],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.myPow(foo, bar)
print(res)
