# https://leetcode.com/problems/minimum-window-substring/description/

# TODO https://neetcode.io/solutions/minimum-window-substring
# TODO write your implementation
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        
        countT, window = {}, {}
        # create a counter for all chars in `t`
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        # `have` is the number of matches `s` has in `t` so far
        # `need` is the number of matches `s` needs in `t`
        have, need = 0, len(countT)
        
        res, shortestLen = [-1, -1], float("infinity")
        
        l = 0
        for idx, ch in enumerate(s):
            # put each char in the window
            window[ch] = window.get(ch, 0) + 1

            # if the char is in `t` and it appears the same amount of times
            # in `s` and in `t`
            if ch in countT and window[ch] == countT[ch]:
                have += 1

            while have == need:
                # if the length of the current matching window is less than the
                # shortest so far
                newLen = idx - l + 1
                if newLen < shortestLen:
                    res = [l, idx]
                    shortestLen = newLen
                    
                winCh = s[l]
                window[winCh] -= 1
                if winCh in countT and window[winCh] < countT[winCh]:
                    have -= 1
                l += 1
                
        l, idx = res
        return s[l : idx + 1] if shortestLen != float("infinity") else ""
    

    
arr = [
    ["ADOBECODEBANC", "ABC"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minWindow(foo, bar)
print(f'res is "{res}"')