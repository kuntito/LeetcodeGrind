# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_map = {}
        uniques = []

        for n in nums:
            if n not in num_map:
                uniques.append(n)
                num_map[n] = 0

            num_map[n] += 1

        uniques.sort(key=lambda n: num_map[n])

        res = []
        while len(res) < k:
            res.append(uniques.pop())

        return res
    

arr = [
    [[1,1,1,2,2,3],  2],
    [[1],  1],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.topKFrequent(foo, bar)
print(res)