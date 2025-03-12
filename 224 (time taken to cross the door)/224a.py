# https://leetcode.com/problems/time-taken-to-cross-the-door/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

class Solution:
    def timeTaken(self, arrival: list[int], state: list[int]) -> list[int]:
        pass
        # you need to know the state of the door at each second
        # since every second, someone passes through the door
        # the doorHistory should be at most the same size as `len(arrival)`
        
        dim = len(arrival)
        doorHistory = [None for _ in range(dim)]
        
        # we only need to check the door history if there's a clash of times
        # makes sense to use a while loop to check for the door times
        # create a temporary array to store indices with similar times
        # pair the indices with their state, (idx, state)


        idx = 0
        # i think it makes sense to create a 2d array, `chunkz`
        # each sub array represents the indices that arrive at the same time
        chunkz = []
        while idx < dim:
            tmp = []
            tmp.append(idx)
            
            # trying to grab consecutive indices with the same arrival time
            while idx + 1 < dim and arrival[idx + 1] == arrival[idx]:
                tmp.append(idx + 1)
                idx += 1
                
            # at this point, `tmp` contains the indices of all the arrivals
            # at the same time
            chunkz.append(tmp)
            idx += 1
            
        print(chunkz)
        
        # use a hashmap to store the index and the time it went in
        timeMap = {}
        currTime = 0
        for sub in chunkz:
            if len(sub) == 1:
                timeMap[sub[0]] = currTime
                currTime += 1
            else:
                pass
                # you need a way to differentiate the indices that want to exit
                # from the entry ones
                # i suggest two lists, so the indices are stored in increasing order
                
            

            
arr = [
    [[0,1,1,2,4], [0,1,0,0,1]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.timeTaken(foo, bar)
print(res)