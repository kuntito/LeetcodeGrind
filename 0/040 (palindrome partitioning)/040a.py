# https://leetcode.com/problems/palindrome-partitioning/description/

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        self.res = []

        self.explore(s, [])

        return self.res
    

    def explore(self, word, arr):
        if word == '':
            self.res.append(arr[::])
            return

        idx = 1
        while idx <= len(word):
            sub_string = word[:idx]
            if self.is_palindrome(sub_string):
                arr.append(sub_string)
                self.explore(word[idx:], arr)
                arr.pop()
            idx += 1


    def is_palindrome(self, word):
        s, e = 0, len(word) - 1

        while s <= e:
            if word[s] != word[e]:
                return False
            s += 1
            e -= 1
            
        return True


arr = [
    "aa",
    "aab",
]
foo = arr[-1]
sol = Solution()
res = sol.partition(foo)

print(res)