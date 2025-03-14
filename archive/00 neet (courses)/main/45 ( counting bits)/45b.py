
class Solution:
    def countBits(self, n: int) -> list[int]:
        arr = [0 for _ in range(n+1)]

        base = 0
        for num in range(1, n + 1):
            if num & (num-1) == 0:
                base = num
            arr[num] = arr[num - base] + 1

        return arr
    
foo = [
    2,
    5,
    8,
]
bar = foo[-1]

sol = Solution()
res = sol.countBits(bar)

print(res)