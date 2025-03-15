# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

# https://neetcode.io/solutions/minimum-operations-to-reduce-x-to-zero
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        pass
        # determine the total sum of `nums`, `totalSum`
        # use sliding window to find every subarray where the [sum == `totalSum - x`]
        # if you find this, find the number of items outside the window
        # track the minimum
        totalSum = sum(nums)
        targetWindowSum = totalSum - x
        
        # TODO is there a way to avoid writing this
        # TODO finish neet's solution 09:17
        if targetWindowSum == 0:
            return len(nums)
        
        tmpSum = 0
        maxWinLen = None
        left = 0
        
        for idx, n in enumerate(nums):
            tmpSum += n
            while tmpSum > targetWindowSum and left < idx:
                tmpSum -= nums[left]
                left += 1
            
            if tmpSum == targetWindowSum:
                winLen = idx - left + 1
                if maxWinLen is None:
                    maxWinLen = winLen
                else:
                    maxWinLen = max(
                        winLen,
                        maxWinLen
                    )
            
            
        res = None
        if maxWinLen is not None:
            res = len(nums) - maxWinLen
        
        return -1 if res is None else res
        
        
arr = [
    [[6016,5483,541,4325,8149,3515,7865,2209,9623,9763,4052,6540,2123,2074,765,7520,4941,5290,5868,6150,6006,6077,2856,7826,9119], 31841],
    [[1,1,4,2,3], 5],
    [[5,6,7,8,9], 4],
    [[3,2,20,1,1,3], 10],
    [[8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365 ],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minOperations(foo, bar)
print(res)