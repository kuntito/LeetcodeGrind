# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

from collections import Counter

class Solution:
    def findConsistentLogs(self, userEvent) -> int:
        events_count = {}
        start = 0
        res = 0

        freq_low = self.get_freq_low(userEvent)

        for idx, e in enumerate(userEvent):
            events_count[e] = events_count.get(e, 0) + 1

            if events_count[e] > freq_low:
                res = max(
                    res,
                    idx - start
                )

                while userEvent[start] != e:
                    events_count[userEvent[start]] -= 1
                    start += 1
                events_count[userEvent[start]] -= 1
                start += 1

        res = max(
            res,
            idx - start + 1,
        )
        return res
    
    def get_freq_low(self, arr):
        frequency = Counter(arr)
        lowest_frequency = min(frequency.values())
        
        return lowest_frequency
    
arr = [
    [1, 2, 1, 3, 4, 2, 4, 3, 3, 4],
    [9, 9, 9],
    [9, 8, 5, 9, 2],
]
foo = arr[-1]
sol = Solution()
res = sol.findConsistentLogs(foo)

print(res)