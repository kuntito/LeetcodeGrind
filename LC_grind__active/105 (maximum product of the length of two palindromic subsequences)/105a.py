# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/description/


# TODO is the solution a brutetforce/backtracking type?
class Solution:
    def maxProduct(self, s: str) -> int:
        pass
        # convert `s` to an array, `arr`
        # find all palindromic subsequences
        # for each sequence, you find
        # start another function call
        # to find the longest palindrome
        # that excludes the indices of the first
        
        dim = len(s)
        self.res = 0
        for idx in range(dim):
            pass
            self.explore_pal(idx, idx, s, set())
            
        for idx in range(1, dim):
            pass
            self.explore_pal(idx-1, idx, s, set())
            
        return self.res
            
            
    def explore_pal(self, left, right, chars, omit):
        dim = len(chars)
        if left < 0 or right == dim:
            return
        leftCh, rightCh = chars[left], chars[right]
            
        if leftCh == rightCh:
            omit.add(left)
            omit.add(right)
            foo = self.explore_omit(chars, omit)
            
            self.res = max(
                len(omit) * foo,
                self.res
            )
            
            self.explore_pal(left-1, right + 1, chars, omit)
        else:
            self.explore_pal(left - 1, right, chars, omit)
            self.explore_pal(left, right + 1, chars, omit)
            
            
    def explore_omit(self, chars, omit):
        dim = len(chars)
        res = 0
        for idx in range(dim):
            res = max(res, self.explore_longest(idx, idx, omit, chars))
            
        for idx in range(1, dim):
            res = max(res, self.explore_longest(idx-1, idx, omit, chars))
        
        return res
    
        
    def explore_longest(self, left, right, omit, chars):
        pass
        dim = len(chars)
        if left < 0 or right == dim:
            return 0
        
        if left in omit:
            return self.explore_longest(left-1, right, omit, chars)
        if right in omit:
            return self.explore_longest(left, right + 1, omit, chars)
        else:
            leftCh, rightCh = chars[left], chars[right]
            
            if leftCh == rightCh:
                return self.explore_longest(left-1, right+1, omit, chars) + 1
            else:
                return max(
                    self.explore_longest(left-1, right, omit, chars),
                    self.explore_longest(left, right + 1, omit, chars),
                )
        
arr = [
    "leetcodecom",
    "bb",
    "accbcaxxcxx"
]
foo = arr[-1]
sol = Solution()
res = sol.maxProduct(foo)
print(res)