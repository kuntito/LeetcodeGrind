class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        
        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)
    
arr = [
    [31, [5,26,18,25,29,21,22,12,19,6], [7,6,6,4,3,4,9,7,6,4]],
]

target, foo, bar = arr[-1]
sol = Solution()

res = sol.carFleet(target, foo, bar)
print(res)