# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        greatest = -1
        for idx in range(len(arr) - 1, -1, -1):
            n = arr[idx]
            arr[idx] = greatest

            greatest = max(n, greatest)

        return arr