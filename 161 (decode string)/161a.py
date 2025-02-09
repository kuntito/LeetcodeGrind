# https://leetcode.com/problems/decode-string/description/

class Solution:
    def decodeString(self, s: str) -> str:
        pass
        # using two pointers,
        # find the last open and the first close
        # using the index of the first open,
        # move leftward and find where the number ends
        # once you have all the details for a token
        # decode it and insert into the string
        # to form a new string
        # recursively call the function on the new string
        # and if no brackets are found
        # return string as is
        return self.explore(s)
    
    def explore(self, chars):
        leftIdx = self.get_last_open(chars)
        if leftIdx is None:
            return chars
        
        rightIdx = self.get_closing_idx(chars, leftIdx)
        numIdx = self.get_num_idx(chars, leftIdx)
        
        decoded = self.decode(numIdx, leftIdx, rightIdx, chars)
        
        # insert into string
        leftSlice = chars[:numIdx]
        rightSlice = chars[rightIdx+1:]
        
        new_string = leftSlice + decoded + rightSlice
        return self.explore(new_string)
    
    def get_last_open(self, chars):
        for idx in range(len(chars)-1, -1, -1):
            if chars[idx] == '[':
                return idx
    
    def get_closing_idx(self, chars, leftIdx):
        for idx in range(leftIdx, len(chars)):
            if chars[idx] == ']':
                return idx
            
    def get_num_idx(self, chars, leftIdx):
        idx = leftIdx
        while idx - 1 >= 0 and chars[idx - 1].isdigit():
            idx -= 1
            
        return idx
    
    def decode(self, numIdx, leftIdx, rightIdx, chars):
        num = int(chars[numIdx:leftIdx])
        
        return num * chars[leftIdx + 1 : rightIdx]
        
arr = [
    "3[a2[c]]",
    "3[a]2[bc]",
    "2[abc]3[cd]ef",
]
foo = arr[-1]
sol = Solution()
res = sol.decodeString(foo)
print(res)