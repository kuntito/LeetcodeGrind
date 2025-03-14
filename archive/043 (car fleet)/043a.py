# https://leetcode.com/problems/car-fleet/description/

from collections import deque

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        count = 0

        # all cars have a starting position
        # which increases by `speed[i]`, `i` is the car index
        # cars can't overtake themselves, if a car starts out behind another
        # it's new position is reduced to match the position of the car in front of it

        while position:
            # put everything in a data structure, `intervals`
            # each item is (startPos, endPos, speed)
            intervals = self.get_intervals(position, speed)

            print(intervals)

            position, speed = self.drive(intervals)

            print("after drive")
            print(position)
            print(speed)


            target_found = False
            while position and position[-1] >= target:
                if position[-1] > target:
                    count += 1
                elif not target_found:
                    count += 1
                    target_found = True
                position.pop()
                speed.pop()

            position, speed = self.join_fleets(position, speed)
            print("after join")
            print(position)
            print(speed)


            print('count is', count)

            break

        return count


    # `drive` should move each car forward,
    # if a car's `newPos` >= `nextCarPos`
    # the car's `newPos` = min(newPos, nextCarPos)
    # the car's `sp` = nextCarSp 
    def drive(self, intervals):
        dim = len(intervals)
        position, speed = deque(), deque()
        for idx in range(dim-1, -1, -1):
            pos, newPos, sp = intervals[idx]

            if position and newPos >= position[0]:
                newPos = min(newPos, position[0])
                sp = speed[0]

            position.appendleft(newPos)
            speed.appendleft(sp)

        return position, speed

    def join_fleets(self, arrPos, arrSpeed):
        position = []
        speed = []

        for pos, sp in zip(arrPos, arrSpeed):
            if not position or pos != position[-1]:
                position.append(pos)
                speed.append(sp)


        return position, speed


    def get_intervals(self, position, speed):
        if len(position) != len(speed):
            raise Exception(f"position({len(position)}) and speed({len(speed)}) are different sizes")
        
        intervals = []
        for pos, sp in zip(position, speed):
            intervals.append((
                pos,
                pos + sp,
                sp
            ))

        intervals.sort()
        return intervals


arr = [
    [13, [10,2,5,7,4,6,11], [7,5,10,5,9,4,1]],
    [100, [0, 2, 4], [4, 2, 1]],
    [10, [8,3,7,4,6,5], [4,4,4,4,4,4]],
    [20, [6, 2, 17], [3, 9, 2]],
    [12, [10,8,0,5,3], [2,4,1,1,3]],
    [10, [0, 4, 2], [2, 1, 3]],
    [10, [8,3,7,4,6,5], [4,4,4,4,4,4]],
    [16, [11,14,13,6], [2,2,6,7]],
    [31, [5,26,18,25,29,21,22,12,19,6], [7,6,6,4,3,4,9,7,6,4]],
    [10, [3], [3]],
    [100, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]],
    [21, [1,15,6,8,18,14,16,2,19,17,3,20,5], [8,5,5,7,10,10,7,9,3,4,4,10,2]],
    #TODO this should return `7` not `8`
]

target, foo, bar = arr[-1]
sol = Solution()

res = sol.carFleet(target, foo, bar)
print(res)