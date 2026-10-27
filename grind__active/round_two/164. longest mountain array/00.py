class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        self.arr = arr
        longest = 0
        for idx, num in enumerate(arr):

            if self.isPeak(idx):
                mountLen = self.getLen(idx)
                if mountLen > longest:
                    longest = mountLen

        return longest


    def getLen(self, idx):
        leftLen = self.getLeftLen(idx)
        rightLen = self.getRightLen(idx)

        return leftLen + rightLen + 1

    def getLeftLen(self, startIdx):
        leftLen = 0
        before = self.arr[startIdx]

        for idx in range(startIdx - 1, -1, -1):
            cur = self.arr[idx]
            if cur >= before:
                break
            
            before = cur
            leftLen += 1


        return leftLen


    def getRightLen(self, startIdx):
        rightLen = 0
        before = self.arr[startIdx]

        dim = len(self.arr)
        for idx in range(startIdx + 1, dim):
            cur = self.arr[idx]
            if cur >= before:
                break

            before = cur
            rightLen += 1

        return rightLen


            
    def isPeak(self, idx):
        arr = self.arr
        dim = len(arr)

        if idx == 0 or (idx == dim - 1):
            return False


        prev = arr[idx - 1]
        after = arr[idx + 1]
        num = arr[idx]

        return prev < num > after


arr = [
    [2,1,4,7,3,2,5],
]
foo = arr[-1]
sol = Solution()

res = sol.longestMountain(foo)
print(res)