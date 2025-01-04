# https://leetcode.com/problems/backspace-string-compare/description/

# TODO https://neetcode.io/solutions/backspace-string-compare
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = self.explore(s)
        b = self.explore(t)

        return a == b

    def explore(self, chars):
        arr = []
        for ch in chars:
            if ch == '#':
                if arr:
                    arr.pop()
                continue

            arr.append(ch)

        return "".join(arr)
    

arr = [
    ["a#c", "b"],
    ["ab##", "c#d#"],
    ["ab#c", "ad#c"],
    ["y#fo##f", "y#f#o##f"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.backspaceCompare(foo, bar)
print(res)