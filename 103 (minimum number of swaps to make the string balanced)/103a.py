# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/

# TODO, is the final answer a brute force/backtracking type solution?
# TODO https://neetcode.io/solutions/minimum-number-of-swaps-to-make-the-string-balanced
# 01:24
class Solution:
    def minSwaps(self, s: str) -> int:
        pass
        # you're only iterating up till half way
        # you only swap when you encounter a closing bracket
        # that doesn't follow an open bracket
        # start a recursive bruteforce function
        # where you swap the closing bracket with an opening one
        # pick the opens from the end of the arr
        # the valid opens are the ones not followed by a close
        # count the number of swaps and track the res
        arr = list(s)
        return self.explore(arr, 0)


    def explore(self, arr, start_idx):
        open_brak, close_brak = '[', ']'

        dim = len(arr)
        dimHalf = dim // 2

        # find the index of the first invalid closing bracket
        # if not exists, return 0
        leftIdx = None
        stack = []
        for idx in range(start_idx, dimHalf):
            # ch = arr[idx]
            # if ch == close_brak:
            #     if idx == 0 or arr[idx - 1] == close_brak:
            #         leftIdx = idx
            #         break

            ch = arr[idx]
            # if ch == open_brak:
            #     stack.append(open_brak)
            # else:
            #     if not stack or stack[-1] == close_brak:
            #         leftIdx = idx
            #         break
                
            #     stack.pop()
            if ch == close_brak:
                leftIdx = idx
                break
                

        if leftIdx is None:
            return 0

        
        
        # iterate from behind, tracking every invalid opening bracket
        # swap it's index with the invalid closing bracket at `leftIdx`
        # start a recursive call with the array with the swapped values
        # store the number of swaps
        
        # swap the indices back `leftIdx, rightIdx` and return the min swaps
        res = None
        stack.clear()
        for rightIdx in range(dim - 1, leftIdx, -1):
            # ch = arr[rightIdx]
            # if ch == open_brak:
            #     if rightIdx == dim - 1 or arr[rightIdx + 1] == open_brak:
            #         arr[leftIdx], arr[rightIdx] = arr[rightIdx], arr[leftIdx]

            #         foo = self.explore(arr, leftIdx)
            #         if res is None:
            #             res = foo
            #         else:
            #             res = min(
            #                 res,
            #                 foo
            #             )


            #         arr[leftIdx], arr[rightIdx] = arr[rightIdx], arr[leftIdx]
            
            ch = arr[rightIdx]
            # to track invalid opens
            # append all closes to the stack
            # if you find and open and the stack is empty or the last val in the stack is an open, then you have found an invalid open
            
            if ch == close_brak:
                stack.append(ch)
            elif stack and stack[-1] == close_brak:
                stack.pop()
            else:
                arr[leftIdx], arr[rightIdx] = arr[rightIdx], arr[leftIdx]
                
                foo = self.explore(arr, leftIdx + 1)
                if res is None:
                    res = foo
                else:
                    res = max(res, foo)
                
                arr[leftIdx], arr[rightIdx] = arr[rightIdx], arr[leftIdx]
                
            
        res = 0 if res is None else res
        return res + 1


arr = [
    "[]",
    "][][",
    "[[[][[]][[[][][]]]]]",
    "]]][[[",
]
foo = arr[-1]
sol = Solution()
res = sol.minSwaps(foo)
print(res)