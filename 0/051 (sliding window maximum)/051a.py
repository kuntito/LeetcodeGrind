# https://leetcode.com/problems/sliding-window-maximum/description/

import heapq


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        elems = nums[:k]
        elems.sort()

        res = []
        maxHeap = []
        for n in elems:
            heapq.heappush(maxHeap, -1 * n)
        res.append(elems[-1])

        to_remove = {}
        rem_idx, idx = 0, k
        while idx < len(nums):
            add = nums[idx]
            heapq.heappush(maxHeap, -1 * add)

            remove = -1 * nums[rem_idx]
            to_remove[remove] = to_remove.get(remove, 0) + 1
            while maxHeap[0] in to_remove and to_remove[maxHeap[0]]:
                to_remove[maxHeap[0]] -= 1
                heapq.heappop(maxHeap)


            res.append(-1 * maxHeap[0])

            rem_idx += 1
            idx += 1

        return res

    

arr = [
    [[1,3,-1,-3,5,3,6,7], 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.maxSlidingWindow(foo, bar)
print(res)