# https://leetcode.com/problems/number-of-ways-to-select-buildings/description/

class Solution:
    def numberOfWays(self, s: str) -> int:
        pass
        # it's looking like a dp problem where you iterate from behind

        # there are two distinct sequences 010 and 101
        # the idea is to create two dp arrays, typOne and typTwo
        
        # typOne is such that for each index `i`
        # it contains the number of `01`s that can be found from that point onwards
        dim = len(s)
        
        # create an array of size `dim`
        # at each index, it stores the number of 0s and 1s
        # from that point onwards
        
        zerosOnes = self.getZerosOnesPrefix(s)
        
        # to get type one, `01`
        typeOne = self.getTypeOne(zerosOnes, s)
        # print(typeOne)
        
        # get type two, `10`
        typeTwo = self.getTypeTwo(zerosOnes, s)
        # print(typeTwo)
        
        res = 0
        for i in range(dim-1):
            bit = s[i]
            if bit == '1':
                res += typeOne[i + 1]
            else:
                res += typeTwo[i + 1]
                
        return res
        
        
    def getTypeTwo(self, zerosOnes, chars):
        pass
        # to get type one, iterate in reverse
        # create result array, `arr`
        
        dim = len(chars)
        arr = [0 for _ in range(dim)]
        
        # for each val that's '1'
        # set `arr[i] = the number of zeros in zerosOnes[i + 1][0]`
        for i in range(dim - 2, -1, -1):
            bit = chars[i]
            if bit == '1':
                arr[i] = zerosOnes[i+1][0]
            arr[i] += arr[i + 1]
                
        return arr

    def getTypeOne(self, zerosOnes, chars):
        pass
        # to get type one, iterate in reverse
        # create result array, `arr`
        
        dim = len(chars)
        arr = [0 for _ in range(dim)]
        
        # for each val that's '0'
        # set `arr[i] = the number of ones in zerosOnes[i + 1][1]`
        for i in range(dim - 2, -1, -1):
            bit = chars[i]
            if bit == '0':
                arr[i] = zerosOnes[i+1][1]
            arr[i] += arr[i + 1]
                
        return arr
            
        
        
    def getZerosOnesPrefix(self, chars):
        zeroCount, oneCount = 0, 0
        
        dim = len(chars)
        arr = [0 for _ in range(dim)]
        
        for i in range(dim - 1, -1, -1):
            val = chars[i]
            if val == '0':
                zeroCount += 1
            else:
                oneCount += 1
                
            arr[i] = (zeroCount, oneCount)
            
        return arr
        
arr = [
    "001101",
    "11100",
]
foo = arr[-1]
sol = Solution()
res = sol.numberOfWays(foo)
print(res)
