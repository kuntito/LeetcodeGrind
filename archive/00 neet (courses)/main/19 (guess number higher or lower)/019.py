# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    choice = 6
    res = choice - num

    return 0 if res == 0 else res//abs(res)


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            num = (left + right)//2
            res = guess(num)
            if res == -1:
                right = num - 1
            elif res == 1:
                left = num + 1
            else:
                return num
            

n = 10
foo = Solution()
res = foo.guessNumber(n)
print(res)