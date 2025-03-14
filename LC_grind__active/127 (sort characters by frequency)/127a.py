# https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        pass
        counter = {}
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1
            
        values = list(counter.items())
        values.sort(key=lambda x: x[1], reverse=True)
        
        res = []
        for ch, count in values:
            for _ in range(count):
                res.append(ch)
        
        return ''.join(res)
        
        
arr = [
    "Tree",
    "Aabb",
]
foo = arr[-1]
sol = Solution()
res = sol.frequencySort(foo)
print(res)