# https://leetcode.com/problems/permutation-in-string/description/



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        arrS1 = [0] * 26
        arrS2 = [0] * 26

        for i in range(len(s1)):
            charOneIdx = self.get_char_idx(s1[i])
            charTwoIdx = self.get_char_idx(s2[i])

            arrS1[charOneIdx] += 1
            arrS2[charTwoIdx] += 1

        matches = 0
        for i in range(26):
            matches += 1 if arrS1[i] == arrS2[i] else 0

        if matches == 26: return True

        for i in range(len(s1), len(s2)):
            prevS2char = s2[i-len(s1)]
            prevS2charIdx = self.get_char_idx(prevS2char)
            arrS2[prevS2charIdx] -= 1

            # if they are equal, you now have a match
            if arrS1[prevS2charIdx] == arrS2[prevS2charIdx]:
                matches += 1
            # if they were equal, you just lost a match
            elif arrS1[prevS2charIdx] == arrS2[prevS2charIdx] + 1:
                matches -= 1

            currCharIdx = self.get_char_idx(s2[i])
            arrS2[currCharIdx] += 1
            if arrS1[currCharIdx] == arrS2[currCharIdx]:
                matches += 1
            elif arrS1[currCharIdx] == arrS2[currCharIdx] - 1:
                matches -= 1

            if matches == 26: return True

        return False


    def get_char_idx(self, ch):
        return ord(ch) - ord('a')
            

        


    
arr = [
    ["ab", "eidboaoo"],
    ["ab", "eidbaooo"],
    ["adc", "dcda"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.checkInclusion(foo, bar)
print(res)

