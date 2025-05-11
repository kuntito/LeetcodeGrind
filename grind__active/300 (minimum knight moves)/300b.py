# https://leetcode.com/problems/minimum-knight-moves/description/


from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        pass
        # how would you implement the bfs for this
        # for one, we'd need a queue to store the current layer of positions
        # for each positions, we explore all eight directions and add them to the queue
        # make sure to not add positions that have been explored
        
        queue = deque()
        origin = (0, 0)
        
        seen = set()
        seen.add(origin)
        queue.append(origin)
        
        steps = 0
        finalDestination = (x, y)
        
        # while queue contains values, technically queue would always contain values since it's an infinite board
        # i guess we'd just use a break statement
        # every time we explore a layer of positions, we increment the steps by `1`
        # it makes sense to declare an integer variable `steps`
        # what increases over time
        
        # we add the origin to queue?
        # does the origin count as a step
        # not exactly, so we can initialize steps to `-1`
        # so the origin parsing increments to `0`
        
        while True:
            # this is the length of the current layer,
            # in the first instance, it is `1`
            dim = len(queue)
            for _ in range(dim):
                pos = queue.popleft()
                if pos == finalDestination:
                    return steps
                
                r, c = pos
                # get the neighbours 
                nextDestinations = [
                    (r - 1, c - 2),
                    (r - 2, c - 1),
                    (r - 1, c + 2),
                    (r - 2, c  +1),
                    (r + 1, c - 2),
                    (r + 2, c - 1),
                    (r + 1, c + 2),
                    (r + 2, c + 1),
                ]
                
                # add the neighbours to the queue
                # exclude any neighbours in seen
                # how do you solve the problem of adding multiple neighbours into the queue
                
                # what if every valid neighbour is added to seen
                # that way we know every position in the queue is unique
                # this would mean we'd add origin to `seen` from the get go
                
                for nei in nextDestinations:
                    if nei in seen: continue
                    queue.append(nei)
                    seen.add(nei)
                
            steps += 1
            
                
arr = [
    [2, 1],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minKnightMoves(foo, bar)
print(res)