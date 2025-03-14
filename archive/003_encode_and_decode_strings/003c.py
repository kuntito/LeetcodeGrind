class Solution:
    def encode(self, strs: list[str]) -> str:
        delim = '#'
        res = [f'{len(word)}{delim}{word}' for word in strs]
        return ''.join(res)

    def decode(self, s: str) -> list[str]:
        delim = '#'
        res, idx = [], 0

        j = 0
        while idx < len(s):
            while s[j] != delim:
                j += 1

            length = int(s[idx:j])
            word = s[j+1: j+1+length]
            res.append(word)

            j += length+1
            idx = j

        return res
    
arr = [
    ["neet","code","love","you"],
    ["we","say",":","yes"],
    ["we","say",":","yes","!@#$%^&*()"],
    [],
    [""],
    ["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"],
]
foo = arr[-1]

sol = Solution()
en = sol.encode(foo)
print(f'`{en}`')

de = sol.decode(en)
print(de)