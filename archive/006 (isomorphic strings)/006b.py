# https://leetcode.com/problems/isomorphic-strings/description/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dim = len(s)
        uno_mapped = set()
        dos_mapped = set()

        mapping = {}
        for idx in range(dim):
            uno = s[idx]
            dos = t[idx]

            if uno in uno_mapped:
                if mapping[uno] != dos: return False
                continue
            elif dos in dos_mapped:
                return False
            
            mapping[uno] = dos
            uno_mapped.add(uno)
            dos_mapped.add(dos)

        return True