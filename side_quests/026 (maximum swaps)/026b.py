# https://leetcode.com/problems/maximum-swap/


class Solution:
    def maximumSwap(self, num: int) -> int:
        pass
        # convert `num` to an array of numbers, `num_arr`
        num_arr = list(str(num))
        dim = len(num_arr)

        # create an array, `greatest_seen` such that for each index
        # the value at that idx is the largest value after that index
        # greatest_seen[idx] = largest number in `num[idx + 1]` and the index of that largest number
        greatest_seen = [-1 for _ in range(dim)]
        greatest = (-1, -1)
        for i in range(dim-1, -1, -1):
            pass
            greatest_seen[i] = greatest
        
            n = int(num_arr[i])
            if n > greatest[0]:
                greatest = (n, i)
        
        # print(greatest_seen)

        
        # loop through the `num_arr` with index
        # if any greatest_seen number is greater than the current value
        # swap them and break the loop
        for idx, n in enumerate(num_arr):
            n = int(n)
            if greatest_seen[idx][0] > n:
                _, target_idx = greatest_seen[idx]
                
                num_arr[idx], num_arr[target_idx] = num_arr[target_idx], num_arr[idx]
                break
        
        
        print(num_arr)
        # return "".join()
        


arr = [
    2736,
    9973,
]
foo = arr[-1]
sol = Solution()
res = sol.maximumSwap(foo)
# print(res)