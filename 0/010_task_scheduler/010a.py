# https://leetcode.com/problems/task-scheduler/description/
import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = Counter(tasks)
        frequency_list = [-count for _, count in counter.items()]
        heapq.heapify(frequency_list)

        count = 0
        while frequency_list:
            count += 1

            item = heapq.heappop(frequency_list)
            freq = item + 1

            if freq < 0:
                count += n
                self.do_subsequent_tasks(n, frequency_list)
                heapq.heappush(frequency_list, freq)

        return count

    def do_subsequent_tasks(self, n, frequency_list):
        count = 0
        removed_items = []
        while frequency_list and count < n:
            count += 1

            item = heapq.heappop(frequency_list)
            freq = item + 1

            if freq < 0:
                removed_items.append(freq)

        for item in removed_items:
            heapq.heappush(frequency_list, item)


arr = [
    [["A","C","A","B","D","B"], 1],
    [["A","A","A","B","B","B"], 3],
    [["A","A"], 2],
    [["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"], 7],
    [["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2],
    [["A","A","A","B","B","B"], 2],
    [["A","A", "B", "C"], 0],
    [["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H","I","I","J","J","K","K","L","L","M","M","N","N","O","O","P","P","Q","Q","R","R","S","S","T","T","U","U","V","V","W","W","X","X","Y","Y","Z","Z"], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.leastInterval(foo, bar)
print(res)

