class Solution:
    def getDistinctGoodnessValues(self, nums):
        self.res = [0]
        self.nums = nums

        seen = set()
        arr = []
        for idx, n in enumerate(self.nums):
            if n in seen: continue
            seen.add(n)
            arr.append(n)
            self.res.append(n)
            self.explore(idx + 1, arr)
            arr.pop()


    
        return sorted(set(self.res))
    
    def explore(self, start_idx, arr):
        if start_idx >= len(self.nums):
            return
        
        seen = set()
        base = arr[-1]
        for idx in range(start_idx, len(self.nums) - 1):
            n = self.nums[idx]
            if n > base and n not in seen:
                seen.add(n)

                arr.append(n)
                self.res.append(sum(arr))
                self.explore(idx + 1, arr)
                arr.pop()

arr = [
    [3, 5, 5, 1],
    [3, 2, 4, 6],
    [4, 2, 4, 1],
]
foo = arr[-1]
sol = Solution()
res = sol.getDistinctGoodnessValues(foo)

print(res)