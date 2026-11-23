from collections import defaultdict

class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        counter = self.getCounter(planks)
        theMost = 0
        for h in counter:
            count = self.howMany(h, counter)
            
            if count > theMost:
                theMost = count
                
        dim = len(planks)
        for i in range(dim):
            for j in range(i+1, dim):
                combo = planks[i] + planks[j]
                
                count = self.howMany(combo, counter)
                if count > theMost:
                    theMost = count
                
        return theMost
    
    def howMany(self, plankHeight, counter):
        count = counter[plankHeight]
        
        counter[plankHeight] -= count
        crumbs = self.getCrumbs(counter)
        counter[plankHeight] += count
        
        countFromCrumbs = self.howManyFromCrumbs(plankHeight, crumbs)
        
        return count + countFromCrumbs
    
    def getCrumbs(self, counter):
        crumbs = []
        for h, freq in counter.items():
            for _ in range(freq):
                crumbs.append(h)
                
        crumbs.sort()
        return crumbs
    
    def howManyFromCrumbs(self, targetLeft, crumbs):
        return self.explore(0, targetLeft, crumbs, [])
    
    def explore(self, startIdx, targetLeft, crumbs, indices):        
        if targetLeft == 0:
            # print(indices)
            for i in indices:
                crumbs[i] = None
            return 1
        
        dim = len(crumbs)
        count = 0
        
        for idx in range(startIdx, dim):
            c = crumbs[idx]
            if c is None: continue
            
            targetLeft -=c
            indices.append(idx)
            
            if len(indices) > 2 or targetLeft < 0:
                indices.pop()
                break
            
            count += self.explore(
                idx + 1,
                targetLeft,
                crumbs,
                indices,
            )
            
            indices.pop()
            targetLeft += c
        
        return count
            
    def getCounter(self, planks):
        counter = defaultdict(int)
        
        for h in planks:
            counter[h] = counter.get(h, 0) + 1
            
        return counter
            
arr = [
    [2,3,7],
    [86,14,46,100],
    [71,2,88,93,15],
    [1,3,2,5,7,5,4,2,1],
    [59,37,55,90,94],
]
foo = arr[-1]
sol = Solution()
res = sol.maximumWidth(foo)
print(f'result is {res}')