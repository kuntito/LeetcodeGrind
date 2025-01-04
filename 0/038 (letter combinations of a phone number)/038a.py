# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        self.char_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        self.res = []
        self.digits = digits
        
        self.explore(0, [])

        return self.res
    
    def explore(self, idx, arr):
        if idx == len(self.digits):
            if arr:
                self.res.append("".join(arr))
            return
        
        digit = self.digits[idx]
        for ch in self.char_map[digit]:
            arr.append(ch)
            self.explore(idx + 1, arr)
            arr.pop()


arr = [
    "2",
    "23",
    "",
]
foo = arr[-1]

sol = Solution()
res = sol.letterCombinations(foo)
print(res)