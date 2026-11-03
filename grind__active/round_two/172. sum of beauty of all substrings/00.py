class Solution:
    def beautySum(self, s: str) -> int:
        dim = len(s)

        beautyCount = 0
        for charCount in range(1, dim + 1):
            for idx in range(dim):
                substr = s[idx:idx + charCount]                
                
                if len(substr) < charCount:
                    break

                c = self.getBeautyCount(substr)
                beautyCount += c
                
                # if c:
                #     print(f'{substr} => {c}')

        return beautyCount

    def getBeautyCount(self, substr):
        mostFreqCount = float("-inf")
        leastFreqCount = float("inf")
        charMap = {}

        for ch in substr:
            charMap[ch] = charMap.get(ch, 0) + 1

            if charMap[ch] > mostFreqCount:
                mostFreqCount = charMap[ch]

        for ch in substr:
            if charMap[ch] < leastFreqCount:
                leastFreqCount = charMap[ch]

        return mostFreqCount - leastFreqCount
        
        
arr = [
    "aabcbaa",
]
foo = arr[-1]
sol = Solution()
res = sol.beautySum(foo)

print(res)