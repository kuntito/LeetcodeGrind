# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        self.seen = set()
        for n in nums:
            self.seen.add(n)

        longest = 0
        for n in nums:
            a = self.explore_left(n - 1, 0)
            b = self.explore_right(n + 1, 0)

            longest = max(longest, a + b + 1)
        
        return longest
    
    def explore_left(self, n, count):
        if n not in self.seen:
            return count
        self.seen.remove(n)
        return self.explore_left(n-1, count + 1)

    def explore_right(self, n, count):
        if n not in self.seen:
            return count
        
        self.seen.remove(n)
        return self.explore_right(n+1, count + 1)

