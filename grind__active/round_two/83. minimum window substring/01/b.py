# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass
        # okay, and how would this go...
        # i'd run through `s` till i find the first t-character
        # that'd be my starting point
        
        # but first, if `t` is a single character
        # and exists in `s`, return `t`
        
        # this is an edgecase? not sure, my thinking is not at it's best today.
        
        # how do i check if a character is in `t`
        # `ch in t`
        
        if len(t) == 1:
            return t if t in s else ""
        
        # now, i've dealt with that case..
        # what am i doing..
        
        # i'd keep iterating through `s`
        # until i find the first t-character
        # and once i find it, i'd keep tracking characters until i match `t`
        
        # it would make sense, to make `t` a set
        # what if t has multiple characters?
        
        # damn... this needs a rewrite..
        # TODO
        startIdx = 0
        
        idx = 0
        while idx < len(s):
            ch = s[idx]
            if ch in t:
                pass
        
