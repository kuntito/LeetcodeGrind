# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:
    def __init__(self, nums: list[int]):
        self.arr = []

        total = 0
        for n in nums:
            total += n
            self.arr.append(total)


    def sumRange(self, left: int, right: int) -> int:
        izquierda_val = self.arr[left - 1] if left > 0 else 0
        derecha_val = self.arr[right]

        return derecha_val - izquierda_val

