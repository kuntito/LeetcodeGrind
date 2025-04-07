# https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3: return False

        # use a while loop
        # every number should start off increasing until you hit the pivot
        # the pivot is the first element that's greater than the next
        # once you find this pivot
        # every element after it should be strictly decreasing

        idx = 1
        dim = len(arr)
        is_increasing = True
        pivot_found = False

        while idx < dim:
            prev = arr[idx - 1]
            curr = arr[idx]

            if pivot_found and is_increasing:
                is_increasing = False

            if is_increasing and prev >= curr:
                return False

            if not is_increasing and prev <= curr:
                return False

            # check for pivot
            if not pivot_found and idx + 1 < dim and arr[idx + 1] < curr:
                pivot_found = True
                idx += 1
                is_increasing = False

            idx += 1


        return not is_increasing            