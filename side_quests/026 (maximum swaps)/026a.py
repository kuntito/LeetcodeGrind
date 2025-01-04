# https://leetcode.com/problems/maximum-swap/
from collections import deque

# TODO  https://www.youtube.com/watch?v=4FZtJ8420m8
class Solution:
    def maximumSwap(self, num: int) -> int:

        num_arr = self.get_num_str(num)
        dim = len(num_arr)

        largest = [None for _ in range(dim)]
        big = [num_arr[-1], dim-1]
        largest[-1] = tuple(big)
        for idx in range(len(num_arr)-2, -1, -1):
            n = num_arr[idx]
            if n > big[0]:
                big[0], big[1] = n, idx

            largest[idx] = tuple(big)


        print(largest)
        for idx in range(dim-1):
            n = num_arr[idx]

            after, after_idx = largest[idx+1]
            if after > n:
                num_arr[idx], num_arr[after_idx] = num_arr[after_idx], num_arr[idx]
                break

        return self.convert_to_num(num_arr)
    
    def convert_to_num(self, num_arr):
        zeros = len(num_arr) - 1
        res = 0

        for n in num_arr:
            res += n * 10 ** zeros
            zeros -= 1

        return res



    def get_num_str(self, num):
        q = deque()
        while num:
            digit = num % 10
            num //= 10

            q.appendleft(digit)

        return q
    
arr = [
    2736,
    9973,
    2739,
]
foo = arr[-1]
sol = Solution()
res = sol.maximumSwap(foo)
print(res)