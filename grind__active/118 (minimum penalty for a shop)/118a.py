# https://leetcode.com/problems/minimum-penalty-for-a-shop/description/

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pass
    
        # at any point, you want to know how many Ns on the left
        # and how many Ys on the right
        
        yes_prefix = self.get_yes_prefix(customers)
        
        no_prefix = self.get_no_prefix(customers)
        
        # print(yes_prefix)
        # print(no_prefix)
        
        dim = len(customers)
        
        res = None
        for idx in range(dim + 1):
            pass
            leftCount = no_prefix[idx - 1] if idx - 1 >= 0 else 0
            rightCount = yes_prefix[idx] if idx < dim else 0
            
            total = leftCount + rightCount
            if res is None:
                res = (total, idx)
            else:
                if total < res[0]:
                    res = (total, idx)
        
        return res[1]
        
    def get_no_prefix(self, customers):
        res = [0 for _ in customers]
        
        count = 0
        for idx, c in enumerate(customers):
            if c == 'N':
                count += 1
            res[idx] = count
            
        return res
    
    def get_yes_prefix(self, customers):
        res = [0 for _ in customers]
        
        count = 0
        dim = len(customers)
        
        for idx in range(dim-1, -1, -1):
            c = customers[idx]
            if c == 'Y':
                count += 1
            res[idx] = count
            
        return res
            
            
arr = [
    "YYNY",
    "NNNNN",
    "YYYY",
]
foo = arr[-1]
sol = Solution()
res = sol.bestClosingTime(foo)
print(res)