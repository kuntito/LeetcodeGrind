# https://leetcode.com/problems/optimal-partition-of-string/description/

class Solution:
    def partitionString(self, s: str) -> int:
        pass
        # this would be a recursive function
        # declare a hashset
        
        # for each unique character
        # iterate through each character of the string
        # maintain a set
        return self.explore(0, s, {})

    def explore(self, start_idx, chars, memo):
        if start_idx in memo:
            return memo[start_idx]
        
        dim = len(chars)
        if start_idx == dim:
            return 0
        
        seen = set()
        res = None
        
        for idx in range(start_idx, dim):
            ch = chars[idx]
            if ch in seen:
                memo[start_idx] = self.explore(idx, chars, memo) + 1
                return memo[start_idx]
            
            seen.add(ch)
            exp_res = self.explore(idx + 1, chars, memo)
            if res is None:
                res = exp_res
            else:
                res = min(exp_res, res)
                
    
        memo[start_idx] = res + 1
        return res + 1
    
arr = [
    "ab",
    "ss",
    "sss",
    "ssssss",
]
foo = arr[-1]
sol = Solution()
res = sol.partitionString(foo)
print(res)