# https://leetcode.com/problems/task-scheduler/description/
import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        arr = [-count for count in Counter(tasks).values()]
        heapq.heapify(arr)

        q = deque()
        count = 0
        while arr or q:
            count += 1

            if arr:
                freq = heapq.heappop(arr)
                freq += 1

                if abs(freq):
                    q.append((count + n, freq))
            
            if q and q[0][0] == count:
                heapq.heappush(arr, q.popleft()[1])


        return count

arr = [
    [["A","C","A","B","D","B"], 1],
    [["A","A","A","B","B","B"], 3],
    [["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"], 7],
    [["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2],
    [["A","A","A","B","B","B"], 2],
    [["A","A", "B", "C"], 0],
    [["A","A"], 2],
    [["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H","I","I","J","J","K","K","L","L","M","M","N","N","O","O","P","P","Q","Q","R","R","S","S","T","T","U","U","V","V","W","W","X","X","Y","Y","Z","Z"], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.leastInterval(foo, bar)
print(res)