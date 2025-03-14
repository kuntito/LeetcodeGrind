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


        for i in range(len(s1), len(s2)):
            if matches == 26: return True

            prevS2char = s2[i-len(s1)]
            prevS2charIdx = self.get_char_idx(prevS2char)
            # if they are equal, decrementing it means i've lost a match
            if arrS1[prevS2charIdx] == arrS2[prevS2charIdx]:
                matches -= 1

            arrS2[prevS2charIdx] -= 1
            # if they are equal, you just gained a match
            if arrS1[prevS2charIdx] == arrS2[prevS2charIdx]:
                matches += 1

            currCharIdx = self.get_char_idx(s2[i])
            # if they are equal, incrementing means i lose a match
            if arrS1[currCharIdx] == arrS2[currCharIdx]:
                matches -= 1

            arrS2[currCharIdx] += 1
            # if they are equal, i've gained a match
            if arrS1[currCharIdx] == arrS2[currCharIdx]:
                matches += 1

        return matches == 26


    def get_char_idx(self, ch):
        return ord(ch) - ord('a')






arr = [
    ["adc", "dcda"],
    ["ab", "eidbaooo"], # TODO why doesn't this return True
]
foo, bar = arr[-1]
sol = Solution()
res = sol.checkInclusion(foo, bar)
print(res)

