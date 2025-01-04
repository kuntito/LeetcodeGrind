class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        uno = self.get_max_sum(0, len(nums), nums)
        dos = uno

        min_start, min_end = self.get_min_sum_subarray(nums)
        if min_end + 1 < len(nums):
            length = len(nums) - (min_end + 1 - min_start)
            dos = self.get_max_sum(
                start = min_end + 1,
                length = length,
                arr=nums,
            )

        return max(uno, dos)

    def get_max_sum(self, start: int, length: int, arr: list[int]):
        best_sum = arr[start]
        temp = 0

        length = min(length, len(arr))
        stop = start + length
        while start < stop:
            n = arr[start % len(arr)]
            temp = max(temp, 0) + n

            best_sum = max(best_sum, temp)
            start += 1

        return best_sum


    def get_min_sum_subarray(self, arr: list[int]):
        min_sum = arr[0]
        temp = 0
        min_start, end = 0, 0

        start = 0

        for idx, n in enumerate(arr):
            if temp > 0:
                temp = 0
                start = idx

            temp += n
            
            if temp < min_sum:
                min_sum = temp
                min_start = start
                end = idx

        return min_start, end
        

arr = [
    [-3, -2, 5, -8],
    [5, -3, 5],
    [1, -2, 3, -2],
    [-3, -2, -3],
    [5,6,1,4,8,-8,7,-5,3],
    [5,-19,10,-15,22,-2,-11,28,-29,10,1,2,22,-23,-9,-30,-6,-9,1,8,24,2,21,29,10,-25,18,30,1,9],
    [88,-35,50,-38,-60,-31,-2,-8,-8,91,-14,50,-25,-26,1,71,-91,-64,-40,46,30,-97,9,-55,-36,-75,71,99,90,-53,-68,-20,-73,89,-14,74,-8,72,82,48,45,2,-42,12,77,22,87,56,73,-21,78,15,-6,-75,24,46,-11,-70,-90,-77,57,43,-66,10,-30,-47,91,-37,-4,-67,-88,19,66,29,86,97,-4,67,54,-92,-54,71,-42,-17,57,-91,-9,-15,-26,56,-57,-58,-72,91,-55,35,-20,29,51,70],
    [88, -35, 50, -147, 91, -14, 50, -51, 72, -195, 76, -97, 9, -166, 260, -214, 89, -14, 74, -8, 249, -42, 327, -21, 93, -81, 70, -248, 100, -66, 10, -77, 91, -196, 297, -4, 121, -146, 71, -59, 57, -141, 56, -187, 91, -55, 35, -20, 150],
    [-3, 5, -3, 1, -2, 9, -3],
]
foo = arr[-1]

# for idx, num in enumerate(foo):
#     print(idx, num)


sol = Solution()
res = sol.maxSubarraySumCircular(foo)
print(res)