# https://leetcode.com/problems/last-stone-weight-ii/description/

# TODO compare with asteroid collision

import heapq
class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        pass
        # to minimize the stones
        # split the stones into two halfs such that we obtain the least absolute difference
        # between the subtotals of both halves
        
        # best case scenario, we have equal subtotals in both halves
        # or one is slightly larger than the other
        
        # if we determine the sum of all stones and divide by 2 rounding down
        # we'd roughly have the halfway point, `halfPoint`
        
        # now what's the best way we can combine stones
        # such that their total is as close to `halfPoint` as possible
        
        # it's looking like a recursive backtracking solution
        # let's sort the list in ascending order
        stones.sort()
        
        total = sum(stones)
        # determine the halfPoint
        halfPoint = total // 2
        
        self.closestSum = 0
        # explore all possible subsets for the closest one
        # avoid re-exploration using a set, the key is (subSum, idx)
        self.explore(0, 0, halfPoint, stones, set())
        
        secondPart = total - self.closestSum
        return secondPart - self.closestSum


    def explore(self, subSum, start_idx, halfPoint, arr, seen):
        mi = (subSum, start_idx)
        if mi in seen:
            return
        
        seen.add(mi)
        
        
        dim = len(arr)
        if start_idx == dim:
            if subSum > self.closestSum:
                self.closestSum = subSum
            return
        
        for idx in range(start_idx, dim):
            n = arr[idx]
            # the reason for this early return is because the list is sorted
            # the algorithm works by picking either picking one item or skipping it
            # at this point, the array is sorted, if we pick the next number, we go overboard
            # if we skip it, we're only going to meet an even greater number or the same number in case of duplicates
            # either way, the recursion ends here
            if subSum + n > halfPoint:
                if subSum > self.closestSum:
                    self.closestSum = subSum
                return
            
            # you can either pick the current number
            self.explore(subSum + n, idx + 1, halfPoint, arr, seen)


            # or ignore it
            self.explore(subSum, idx + 1, halfPoint, arr, seen)
        
        


arr = [
    [89,23,100,93,82,98,91,85,33,95,72,98,63,46,17,91,92,72,77,79,99,96,55,72,24,98,79,93,88,92],
    [1],
    [2,7,4,1,8,1],
    [31,26,33,21,40],
]
foo = arr[-1]
sol = Solution()
res = sol.lastStoneWeightII(foo)
print(res)