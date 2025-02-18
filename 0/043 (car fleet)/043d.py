# https://leetcode.com/problems/car-fleet/description/


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pass
        # combine `position` and `speed`
        # sort by `(position, speed)`
        # iterate through the combined arr in reverse
        # calculate the time each car would take to reach the destination
        # add it to `res`
        combined = []
        for p, s in zip(position, speed):
            combined.append((p, s))
            
        combined.sort(key=lambda x: (x[0], x[1]))
        
        # for subsequent cars
        # only add their time to res, if their time is less than res[-1]
        dim = len(position)
        res = []
        for idx in range(dim - 1, -1, -1):
            p, s = combined[idx]
            
            dist = target - p
            targetTime = dist / s
            
            if not res or targetTime > res[-1]:
                res.append(targetTime)
            
        
        return len(res)
    
    
arr = [
    [12, [10,8,0,5,3], [2,4,1,1,3]],
    [100, [0, 2, 4], [4, 2, 1]],
    [10, [3], [3]],
    # [31, [5,26,18,25,29,21,22,12,19,6], [7,6,6,4,3,4,9,7,6,4]],
    [21, [1,15,6,8,18,14,16,2,19,17,3,20,5], [8,5,5,7,10,10,7,9,3,4,4,10,2]],
    [31, [5,26,18,25,29,21,22,12,19,6], [7,6,6,4,3,4,9,7,6,4]],
]

target, foo, bar = arr[-1]
sol = Solution()

res = sol.carFleet(target, foo, bar)
print(res)