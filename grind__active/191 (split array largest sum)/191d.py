# https://leetcode.com/problems/split-array-largest-sum/

# i'm given an integer array, `nums`
# i want to split `nums` into `k` subarrays

# such that all subarrays have at least one value
# and the subarrays with multiple values must be contiguous values of `nums`

# there's multiple ways to achieve this split
# in every split, there's a subarray with the largest sum

# of these largest sum subarrays, we want to return the least

# it's very similar to the 'put marbles in bag' question

# i'm thinking of `k` as the number of bags
# each bag can contain one or more numbers

# we can explore all possibilities using recursive calls
# we'd start by placing one number in the bag, decrement `k`
# start another recursive call and place another number in the bag
# if we run out of bags without running out of numbers
# we end the recursive call

# we'd restart the recursive call and we increase the numbers in the bag by `1`
# and continue the recursion

# i've implemented the different splits
# now, i need to track the largest subarray in each one
# how do i do that?

# for every split, i sum up each subarray
# and track the highest by passing the subarray sum in subsequent recursive calls
# and at the end, i update a global variable for leastHighest

# it works so far
# i can optimize the subarray sums using a prefix sum
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        pass

        self.nums = nums

        start, end = 0, 0
        numBags = k

        arr = []
        self.leastHighest = float("inf")
        
        self.prefixSum = self.getPrefixSum(nums)
        
        self.explore(start, end, numBags, arr, 0)
        
        return self.leastHighest
    
    def getPrefixSum(self, arr):
        prefix = []
        
        acc = 0
        for n in arr:
            acc += n
            prefix.append(acc)
            
        return prefix

    def explore(self, start, end, numBags, arr, curSum):
        isExhaustNumbers = end == len(self.nums)
        isExhaustBags = numBags == 0

        if isExhaustNumbers and isExhaustBags:
            print(arr, end=" ")
            print(curSum)
            self.leastHighest = min(curSum, self.leastHighest)
            return

        if isExhaustNumbers or isExhaustBags:
            return

        self.explore(start, end + 1, numBags, arr, curSum)

        # arr.append(self.nums[start : end + 1])
        
        leftSum = self.prefixSum[start - 1] if start - 1 >= 0 else 0
        rightSum = self.prefixSum[end]
        subArrSum = rightSum - leftSum
        self.explore(end + 1, end + 1, numBags - 1, arr, max(curSum, subArrSum))
        # arr.pop()


arr = [
    [[1, 2, 3], 2],
    [[1, 2, 3, 4, 5], 2],
    [[7,2,5,10,8], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)
