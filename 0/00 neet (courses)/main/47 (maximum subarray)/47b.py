
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums: return

        best_start, end = 0, 1
        start = 0

        temp = 0
        biggest_sum = nums[start]
        for idx, n in enumerate(nums):
            if temp < 0:
                temp = n
                start = idx
            else:
                temp += n

            if temp > biggest_sum:
                biggest_sum = temp
                best_start = start
                end = idx+1
        
        return sum(nums[best_start:end])

    def neetSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        maxL, maxR = 0, 0
        L = 0

        for R in range(len(nums)):
            if curSum < 0:
                curSum = 0
                L = R

            curSum += nums[R]
            if curSum > maxSum:
                maxSum = curSum
                maxL, maxR = L, R

        return sum(nums[maxL: maxR+1])

arr = [
    [2, 3],
    [5,4,-1,7,8],
    [-2,1,-3,4,-1,2,1,-5,4],
    [0, 5, 8, -9, 9, -7, 3, -2],
    [-1, -2],
]
foo = arr[-1]

sol = Solution()
res = sol.maxSubArray(foo)

print(res)