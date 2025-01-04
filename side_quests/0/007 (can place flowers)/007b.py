# https://leetcode.com/problems/can-place-flowers/description/


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        dim = len(flowerbed)
        idx = 0
        
        # you can only place a flower if the position behind it is vacant
        # and the position in front of it is vacant
        for idx in range(dim):
            if n == 0: return True

            pos = flowerbed[idx]
            
            leftIdx = idx -1
            rightIdx = idx + 1
            is_left_vacant = leftIdx == -1 or flowerbed[leftIdx] == 0
            is_right_vacant = rightIdx == dim or flowerbed[rightIdx] == 0

            if pos == 0 and is_left_vacant and is_right_vacant:
                flowerbed[idx] = 1
                n -= 1

        return n == 0

arr = [
    [[1,0,0,0,1], 1],
    [[1,0,0,0,1], 2],
    [[0,0,1,0,0], 1],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.canPlaceFlowers(foo, bar)
print(res)