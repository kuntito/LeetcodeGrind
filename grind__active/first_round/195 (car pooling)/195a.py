# https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        pass
    
        # create a list and sort by (time, then drop) 
        # `pick_or_drop` is a number, 1 means pick
        # 0 means drop
        
        # create variable `currCapacity`
        # this should never go over `capacity`
        # if you ever attempt to pick up more passengers than possible
        # return False

        arr = []
        for person, src, dst in trips:
            arr.append(
                (src, 1, person)
            )
            arr.append(
                (dst, 0, person)
            )
        
        
        arr.sort(key=lambda x: (x[0], x[1]))
        
        currCapacity = 0
        for _, pick_or_drop, person in arr:
            pass
            if pick_or_drop == 1:
                currCapacity += person
            else:
                currCapacity -= person
                
            if currCapacity > capacity:
                return False
        
        return True
    
arr = [
    [[[2,1,5],[3,3,7]], 4],
    [[[2,1,5],[3,3,7]], 5],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.carPooling(foo, bar)
print(res)