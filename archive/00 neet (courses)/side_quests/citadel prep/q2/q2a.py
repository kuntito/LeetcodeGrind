class Solution:
    def getMaximumPower(self, power) -> int:
        self.power_map = {}
        for p in power:
            self.power_map[p] = self.power_map.get(p, 0) + p

        self.keys = sorted(self.power_map.keys())
        best = 1
        self.best_power = [0 for _ in self.keys]
        for idx in range(len(self.keys)-1, -1, -1):
            p = self.keys[idx]

            best_after = self.get_best_power_after(p, idx)
            self.best_power[idx] = self.power_map[p] + best_after
            best = max(
                best,
                self.best_power[idx]
            )

        return best
    

    def get_best_power_after(self, p, idx):
        if idx + 1 >= len(self.best_power) or\
        idx + 2 >= len(self.best_power):
            return 0
        
        if self.keys[idx + 1] > p + 1:
            return self.best_power[idx + 1]
    
        return self.best_power[idx + 2]



arr = [
    [1, 2, 3, 4, 5],
    [3, 3, 3, 4, 4, 1, 8],
    [1, 1, 1, 2],
]
foo = arr[-1]
sol = Solution()
res = sol.getMaximumPower(foo)
print(res)