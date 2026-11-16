from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        hashmap = defaultdict(int)

        beginIdx = 0
        otherIdx = 0

        res = 0

        for n in nums:
            hashmap[n] += 1

            while len(hashmap) > k:
                beginNum = nums[otherIdx]
                hashmap[beginNum] -= 1
                if hashmap[beginNum] == 0:
                    hashmap.pop(beginNum)

                otherIdx += 1
                beginIdx = otherIdx

            while hashmap[nums[otherIdx]] > 1:
                hashmap[nums[otherIdx]] -= 1
                otherIdx += 1

            if len(hashmap) == k:
                subarrsWithinWindow = otherIdx - beginIdx + 1
                res += subarrsWithinWindow

        return res

            
arr = [
    [[1, 2, 3], 2],
    [[1, 2, 1, 2, 3], 2],
    [[2,1,1,1,2], 1],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.subarraysWithKDistinct(foo, bar)
print(res)