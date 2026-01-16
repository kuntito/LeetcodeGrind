# https://leetcode.com/problems/excel-sheet-column-title/

# TODO watch https://www.youtube.com/watch?v=X_vJDpCCuoA, 02:48
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        self.num_to_alpha = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J",
            11: "K",
            12: "L",
            13: "M",
            14: "N",
            15: "O",
            16: "P",
            17: "Q",
            18: "R",
            19: "S",
            20: "T",
            21: "U",
            22: "V",
            23: "W",
            24: "X",
            25: "Y",
            0: "Z",
        }

    def explore(self, number, res):
        pass
    
arr = [
    1,
    28,
    26,
]

foo = arr[-1]
sol = Solution()
res = sol.convertToTitle(foo)
print(res)