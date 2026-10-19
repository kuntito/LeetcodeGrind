class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        posNum = 1
        for n in arr:
            while posNum != n:
                k -= 1
                posNum += 1

                if k == 0:
                    return posNum - 1
                
            posNum += 1
 

        return arr[-1] + k

arr = [
    [
        [1, 2, 3, 4],
        2,
    ],
    # [
    #     [2,3,4,7,11],
    #     5,
    # ],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.findKthPositive(foo, bar)
print(res)