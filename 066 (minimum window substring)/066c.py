# https://leetcode.com/problems/minimum-window-substring/description/

# TODO https://neetcode.io/solutions/minimum-window-substring
# TODO deep solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        
        countT, window = {}, {}
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in countT and window[ch] == countT[ch]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""