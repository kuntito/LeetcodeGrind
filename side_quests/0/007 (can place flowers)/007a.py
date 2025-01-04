# https://leetcode.com/problems/can-place-flowers/description/


# TODO https://neetcode.io/solutions/can-place-flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        dim = len(flowerbed)
        idx = 0
        
        while idx < dim and n:
            spot = flowerbed[idx]
            if spot == 0 and self.is_valid(idx, flowerbed):
                flowerbed[idx] = 1
                n -= 1
            idx += 1

        return n == 0
                
    def is_valid(Self, idx, flowerbed):
        left = idx - 1
        right = idx + 1

        is_left_valid = left == -1 or flowerbed[left] == 0
        is_right_valid = right == len(flowerbed) or flowerbed[right] == 0

        return is_left_valid and is_right_valid

arr = [
    [[1,0,0,0,1], 1],
    [[1,0,0,0,1], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.canPlaceFlowers(foo, bar)
print(res)