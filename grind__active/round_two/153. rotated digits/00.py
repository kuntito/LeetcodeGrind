class Solution:
    def rotatedDigits(self, n: int) -> int:
        self.rotate_map = {
            0: 0,
            1: 1,
            2: 5,
            3: None,
            4: None,
            5: 2,
            6: 9,
            7: None,
            8: 8,
            9: 6,
        }

        res = []
        for i in range(1, n + 1):
            is_good = self.is_good_integer(i)

            if is_good:
                res.append(i)

        return len(res)

    def is_good_integer(self, num):
        rotated_num = self.rotate(num)

        return rotated_num != num and rotated_num is not None

    def rotate(self, num):
        rotated_num = ""

        for dig in str(num):
            x = self.rotate_map[int(dig)]
            if x is None:
                return None

            rotated_num += str(x)

        return int(rotated_num)

arr = [
    10,
    2,
]
foo = arr[-1]
sol = Solution()
res = sol.rotatedDigits(foo)

print(res)