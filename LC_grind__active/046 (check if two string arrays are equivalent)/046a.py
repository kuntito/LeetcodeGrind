# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/

# TODO https://neetcode.io/solutions/check-if-two-string-arrays-are-equivalent
class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        # four pointers
        # two pointers for the each word in `word1` and `word2`, `wordUnoIdx`, `wordDosIdx`
        # and two pointers, `unoIdx` and `dosIdx` for matching characters
        # `unoIdx` and `dosIdx` always move by `1` in each iteraction
        # if either index reaches the last character of their respective words
        # move to the next word, reset the index to `0` and continue the comparison
        

        w_uno_idx, w_dos_idx = 0, 0
        uno, dos = 0, 0

        while w_uno_idx < len(word1) and w_dos_idx < len(word2):
            wordUno, wordDos = word1[w_uno_idx], word2[w_dos_idx]
            chOne, chTwo = wordUno[uno], wordDos[dos]
            if chOne != chTwo:
                return False

            uno += 1
            dos += 1

            if uno == len(wordUno):
                uno = 0
                w_uno_idx += 1
            
            if dos == len(wordDos):
                dos = 0
                w_dos_idx += 1

        return uno == dos and w_uno_idx == len(word1) and w_dos_idx == len(word2)
    
arr = [
    [["a", "cb"], ["ab", "c"]],
    [["ab", "c"], ["a", "bc"]],
    [["abc", "d", "defg"], ["abcddefg"]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.arrayStringsAreEqual(foo, bar)
print(res)