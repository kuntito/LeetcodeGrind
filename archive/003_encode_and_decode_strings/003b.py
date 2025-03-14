from collections import deque

class Solution:
    def encode(self, strs: list[str]) -> str:
        delim = '#'
        res = [f'{len(word)}{delim}{word}' for word in strs]
        return ''.join(res)

    def decode(self, s: str) -> list[str]:
        res = []
        delim = '#'

        delim_found = False
        temp = ''
        count = None
        for ch in s:
            if ch == delim and not delim_found:
                count = int(temp)
                if not count: res.append('')
                delim_found = True if count else False
                temp = ''
                continue

            temp += ch
            if delim_found and len(temp) == count:
                delim_found = False
                res.append(temp)
                temp = ''

        if delim_found:
            res.append(temp)

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