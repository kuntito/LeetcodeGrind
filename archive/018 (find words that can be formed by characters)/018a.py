# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_map = {}
        for ch in chars:
            char_map[ch] = char_map.get(ch, 0) + 1

        res = 0
        for w in words:
            if self.is_match(w, char_map):
                res += len(w)
        return res
    
    def is_match(self, word, char_map):
        foo = {}
        for ch in word:
            if ch not in char_map:
                return False
            foo[ch] = foo.get(ch, 0) + 1
            if foo[ch] > char_map[ch]:
                return False
            
        return True