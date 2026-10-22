class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        arr = []
        # TODO start here, see if you can optimize.
        # it was a pain to write this one go.
        # one point is the logic for all branches
        # another is for the subarrays.
        # but there might be some way to not have to check all subarrays.
        # and a way to reuse the logic across each path.
        
        # TODO see if you can do this without the global count
        self.count = 0
        self.dim = zero + one
        
        self.zeroCount = zero
        self.oneCount = one
        self.minSubArrSize = limit + 1
        
        idx = 0
        self.explore(idx, arr)
        
        return self.count
    
    def explore(self, curIdx, arr):
        if self.isOutOfBounds(curIdx):
            if self.checkIsValid(arr):
                # print(arr)
                self.count += 1
            return
        
        arr.append(0)
        self.explore(curIdx + 1, arr)
        arr.pop()
        arr.append(1)
        self.explore(curIdx + 1, arr)
        arr.pop()
        
    def checkIsValid(self, arr):
        zeroCount = sum(1 for x in arr if x == 0)
        if zeroCount != self.zeroCount:
            return False
        
        oneCount = sum(1 for x in arr if x == 1)
        if oneCount != self.oneCount:
            return False
        
        # TODO first of all here, i only need to check subarrays of size, `minSubArrSize`
        # since any larger sub arrays would include the smaller ones.
        for subSize in range(self.minSubArrSize, self.dim + 1):
            i = 0
            while True:
                slice = arr[i: i + subSize]

                if len(slice) < self.minSubArrSize:
                    break

                if not self.hasBothZeroAndOne(slice):
                    return False
                i += 1
                
        return True
    
    def hasBothZeroAndOne(self, arr):
        oneSeen = False
        zeroSeen = False
        for x in arr:
            if x == 0:
                zeroSeen = True
                
            if x == 1:
                oneSeen = True
                
            if zeroSeen and oneSeen:
                return True
            
        return False
        
    def isOutOfBounds(self, curIdx):
        return curIdx >= self.dim
        
        
arr = [
    [1, 1, 2],
    [1, 2, 1],
    [3, 3, 2],
]
foo, bar, baz = arr[-1]
sol = Solution()

res = sol.numberOfStableArrays(foo, bar, baz)
print(res)