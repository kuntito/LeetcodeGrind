# https://leetcode.com/problems/squares-of-a-sorted-array/description/

# TODO https://neetcode.io/solutions/squares-of-a-sorted-array
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # create an array for the result, `res`
        # two pointers, `negPointer`, `posPointer`
        # `negPointer` starts at the first negative number
        # `posPointer` starts at the first positive number
        # create a while loop that runs when both pointers are valid
        # `negPointer` becomes invalid when ...

        # `posPointer` becomes invalid when it reaches the end of the `nums`

        # on each iteration, compare the absolute values at both pointers
        # the lesser one, should be square and appended to `res`

        dim = len(nums)

        posPointer = 0
        while posPointer < dim and nums[posPointer] < 0:
            posPointer += 1

        negPointer = posPointer -1            

        res = []
        while negPointer > -1 and posPointer < dim:
            neg, pos = abs(nums[negPointer]), abs(nums[posPointer])
            if neg < pos:
                res.append(neg ** 2)
                negPointer -= 1
            else:
                res.append(
                    pos ** 2
                )
                posPointer += 1

        while negPointer > -1:
            res.append(
                nums[negPointer] ** 2
            )
            negPointer -= 1

        while posPointer < dim:
            res.append(
                nums[posPointer] ** 2
            )
            posPointer += 1

        return res



arr = [
    [-4,-1,0,3,10],
]
foo = arr[-1]
sol = Solution()
res = sol.sortedSquares(foo)
print(res)