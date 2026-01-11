# https://leetcode.com/problems/valid-parenthesis-string/description/

import sys

# TODO i think this would work asides TLE
class Solution:
    def checkValidString(self, s: str) -> bool:
        pass
        # turn `s` to an array, `arr`
        arr = list(s)

        # id all the indices with asterisks
        slots = [idx for idx, ch in enumerate(s) if ch == '*']
        if len(slots) == len(arr):
            return True
        
        # recursively place '(', ')' and ''

        # the memo key should be what the previous slots contained + the new type
        memo = {}
        
        a = self.explore('(', 0, slots, arr, "", memo)
        if a:
            return a
        b = self.explore('', 0, slots, arr, "", memo)
        if b:
            return b
        
        return self.explore(')', 0, slots, arr, "", memo)

        # when all slots are exhausted, check the arr for a valid parenthesis string
        
    def explore(self, type, slot_idx, slots, arr, prior, memo):
        prior += type
        foo = (prior, slot_idx)
        if foo in memo:
            return memo[foo]
        
        if slot_idx == len(slots):
            x = self.validate(arr)
            return x

        arr_idx = slots[slot_idx]
        
        arr[arr_idx] = type
        a = self.explore('(', slot_idx + 1, slots, arr, prior, memo)
        if a:
            memo[foo] = a
            return memo[foo]
        
        b = self.explore('', slot_idx + 1, slots, arr, prior, memo)
        if b:
            memo[foo] = b
            return memo[foo]
        
        memo[foo] = self.explore(')', slot_idx + 1, slots, arr, prior, memo)
        return memo[foo]


    def validate(self, arr):
        # print(''.join(arr))
        # sys.exit()
        stack = []
        for ch in arr:
            if ch == '':
                continue

            if ch == ')':
                if not stack or stack.pop() != '(':
                    return False
            else:
                stack.append(ch)

        return not stack

    

arr = [
    "(**()",
    "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()",
    "**************************************************))))))))))))))))))))))))))))))))))))))))))))))))))",
    "************************************************************",
]
foo = arr[-1]
sol = Solution()
res = sol.checkValidString(foo)
print(res)

# chars = "(((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))"
# res  = sol.validate(chars)
# print(res)