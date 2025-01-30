# https://leetcode.com/problems/isomorphic-strings/description/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dim = len(s)
        dos_mapped = set()

        mapping = {}
        for idx in range(dim):
            uno = s[idx]
            dos = t[idx]

            # if mapping is valid, continue
            if uno in mapping and mapping[uno] == dos:
                continue

            # at this point, either `uno` has not been mapped
            # or `uno` has been mapped to another character apart from `dos`

            # if `uno` is not mapped and `dos` is mapped, return False
            a = dos in dos_mapped

            # `uno in mapping` means it's been mapped to another character apart from `dos`
            b = uno in mapping 
            if a or b:
                return False
            
            mapping[uno] = dos
            dos_mapped.add(dos)

        return True


            



    
arr = [
    ["egg", "add"],
    ['badc', 'baba'],
    ["bbbaaaba", "aaabbbba"],
    ["foo", "bar"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.isIsomorphic(foo, bar)
print(res)