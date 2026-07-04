class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestStreak = 0
        for idx, ch in enumerate(s):
            streakLen = self.exploreStreak(idx, k, s)
            
            longestStreak = max(
                longestStreak,
                streakLen,
            )

        return longestStreak
    
    
    def exploreStreak(self, startIdx, replacementsLeft, s):
        startCh = s[startIdx]
        dim = len(s)
        streakLen = 0
        for idx in range(startIdx, dim):
            ch = s[idx]
            if ch == startCh:
                pass
            elif replacementsLeft > 0:
                replacementsLeft -= 1
            else:
                break
            
            streakLen += 1
            
        return streakLen