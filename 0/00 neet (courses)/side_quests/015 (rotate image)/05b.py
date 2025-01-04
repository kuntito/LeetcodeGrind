class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        primera, segundo = 0, len(matrix) - 1
        while primera < segundo:

            for step in range(segundo - primera):
                top_left = matrix[primera][primera + step]

                matrix[primera][primera + step] = matrix[segundo - step][primera]

                matrix[segundo - step][primera] = matrix[segundo][segundo - step]

                matrix[segundo][segundo - step] = matrix[primera + step][segundo]

                matrix[primera + step][segundo] = top_left

            primera += 1
            segundo -= 1

arr = [
    [
        [1, 2],
        [3, 4],
    ],
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16],
    ],
    [
        [2,29,20,26,16,28],
        [12,27,9,25,13,21],
        [32,33,32,2,28,14],
        [13,14,32,27,22,26],
        [33,1,20,7,21,7],
        [4,24,1,6,32,34],
    ],
]
foo = arr[-1]

sol = Solution()
sol.rotate(foo)


for row in foo:
    print(row)
