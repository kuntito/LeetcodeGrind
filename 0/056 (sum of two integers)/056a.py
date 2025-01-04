# https://leetcode.com/problems/sum-of-two-integers/submissions/


class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        shift = 0
        res = 0

        while a or b:
            bitOne = a & 1
            bitTwo = b & 1

            a >>= 1
            b >>= 1

            arr = [bitOne, bitTwo, carry]
            arr.sort()
            total = self.add(arr)
            carry = self.get_carry(arr)

            for _ in range(shift):
                total <<= 1
            
            res |= total
            shift += 1


        for _ in range(shift):
            carry <<= 1
        
        res |= carry

        return res
    

    def add(self, arr):
        return arr[0] ^ arr[1] ^ arr[2]

    def get_carry(self, arr):
        return 1 if arr[1] == 1 else 0
        

# TODO TLE occurs wuth negative numbers because they have infinte length in Python?
arr = [
    [3, 2],
    [122, 1,]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.getSum(foo, bar)
print(res)

