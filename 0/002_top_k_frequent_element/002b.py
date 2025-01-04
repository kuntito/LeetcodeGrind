class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_map = {}
        for n in nums:
            if n not in num_map:
                num_map[n] = 0
            num_map[n] += 1


        bucket = [[] for _ in range(len(nums))]
        for n, freq in num_map.items():
            bucket[freq-1].append(n)

        res = []
        while len(res) < k:
            lst = bucket.pop()
            while lst and len(res) < k:
                res.append(lst.pop())

        return res

arr = [
    [[1],  1],
    [[1,1,1,2,2,3],  2],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.topKFrequent(foo, bar)
print(res)