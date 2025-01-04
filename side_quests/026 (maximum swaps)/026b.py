# https://leetcode.com/problems/maximum-swap/


class Solution:
    def maximumSwap(self, num: int) -> int:
        pass
        # convert `num` to an array of numbers, `num_arr`
        num_arr = list(str(num))

        # create an array, `greatest_seen` such that for each index
        # the value at that idx is the largest value after that index
        # greatest_seen[idx] = largest number in `num[idx + 1]` and the index of that largest number
        
        # loop through the `num_arr` with index
        # if any greatest_seen number is greater than the current value
        # swap them and break the loop
        


arr = [
    2736,
]
foo = arr[-1]
sol = Solution()
res = sol.maximumSwap(foo)
# print(res)