class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        self.mostOccur = 1
        self.sums = []

        self.explore(planks)

        return self.mostOccur

    def updateMostOccur(self):
        counter = {}
        res = 0

        for n in self.sums:
            counter[n] = counter.get(n, 0) + 1
            if counter[n] > res:
                res = counter[n]

        if res > self.mostOccur:
            self.mostOccur = res

    def explore(self, planks):
        summ = 0
        for idx, n in enumerate(planks):
            if n is None: continue

            print(n)

            summ += n
            planks[idx] = None

            self.sums.append(summ)

            self.explore(planks)

            self.sums.pop()
            planks[idx] = n

        self.updateMostOccur()

# TODO start here, you algo doesn't look at combinations.
# it explores 23, 23 + 90, but never 23 + 67
arr = [
    [23,90,67,60],
]
foo = arr[-1]
sol = Solution()
res = sol.maximumWidth(foo)

print(res)