from collections import deque

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        q = deque()
        q.append([])
        for n in nums[::-1]:
            for _ in range(len(q)):
                sub = q.popleft()
                for idx in range(len(sub) + 1):
                    sub_copy = sub.copy()
                    sub_copy.insert(idx, n)
                    q.append(sub_copy)

        while q:
            res.append(q.popleft())

        return res

arr = [
    [1, 2, 3],
]

foo = arr[-1]
sol = Solution()
res = sol.permute(foo)
print(res)