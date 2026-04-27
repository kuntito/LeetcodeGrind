import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # first, i'd sort
        # then grab the gaps

        nums.sort()
        minHeap = []

        for idx, n in enumerate(nums):
            if idx == 0:
                continue

            # how do you know if there's a gap?
            # if the current number is greater than the previous number
            # with two or more integers

            curNum = nums[idx]
            prevNum = nums[idx - 1]
            isGap = curNum >= (prevNum + 2)

            if isGap:
                # then we store the gap
                # how do we store the gap?
                # since, we want to address it by size
                # we use a min heap

                # each item is (gapSize, gapStart)
                gapSize = curNum - 1 - prevNum
                gapStart = prevNum + 1

                heapq.heappush(
                    minHeap,
                    (gapSize, gapStart)
                )

        # now, i'd have all the gaps
        
        count = 0
        while minHeap:
            smallestGap = heapq.heappop(minHeap)
            gapSize, gapStart = smallestGap
            
            # once, you fill the gap
            # the question becomes, what's the size of the current interval?
             
        
        return count
arr = [
    [7, 2, 5]
]
foo = arr[-1]
sol = Solution()
res = sol.minOperations(foo)
