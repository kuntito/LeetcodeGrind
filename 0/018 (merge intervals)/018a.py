class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        res = []

        item = intervals[0]
        for idx in range(1, len(intervals)):
            _, e = item
            ns, ne = intervals[idx]

            if e < ns:
                res.append(item)
                item = intervals[idx]
            else:
                item[1] = max(e, ne)
        
        res.append(item)

        return res



arr = [
    [[1,3],[2,6],[8,10],[15,18]],
    [[1,4],[4,5]],
    [[1,4],[2,3]],
]
foo = arr[-1]
sol = Solution()
res = sol.merge(foo)

print(res)