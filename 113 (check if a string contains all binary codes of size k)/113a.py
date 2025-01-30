# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

# TODO rewrite this such that you can memoize it
# TODO is there a faster alternative?
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        pass
        if k > len(s):
            return False
        
        # get all binary codes of size `k`
        # check if they're in `s`
        return self.explore([], k, s, {})
    
    def explore(self, arr, max_len, s, memo):
        foo = ''.join(arr)
            
        if foo and foo in memo:
            return memo[foo]
        
        pass
        if len(arr) == max_len:
            concat = ''.join(arr)
            return concat in s
    
        arr.append("1")
        if not self.explore(arr, max_len, s, memo):
            if foo:
                memo[foo] = False
            return False
        arr.pop()

        arr.append("0")
        if not self.explore(arr, max_len, s, memo):
            if foo:
                memo[foo] = False
            return False
        arr.pop()
        
        if foo:
            memo[foo] = True
        return True
        
arr = [
    ["00110110", 2],
    ["0110", 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.hasAllCodes(foo, bar)
print(res)
        