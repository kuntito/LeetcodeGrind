# https://leetcode.com/problems/first-bad-version/description/

def isBadVersion(n):
    return n >= 1

class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n

        while left <= right:
            mid = (left + right)//2
            if isBadVersion(mid):
                if isBadVersion(mid-1):
                    right = mid - 1
                else:
                    return mid
            else:
                left = mid + 1

n = 5
n = 1

foo = Solution()
res = foo.firstBadVersion(n)

print(res)