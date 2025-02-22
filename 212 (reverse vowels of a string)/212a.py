# https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s: str) -> str:
        pass
        # iterate through the string
        # grab all the vowels and their indices
        vowels_found = []
        arr = list(s)
        
        vowels = "aeiou"
        for idx, ch in enumerate(arr):
            if ch.lower() in vowels:
                vowels_found.append((ch, idx))
                
        left, right = 0, len(vowels_found) - 1
        
        while left < right:
            leftCh, leftIdx = vowels_found[left]
            rightCh, rightIdx = vowels_found[right]
            
            arr[leftIdx] = rightCh
            arr[rightIdx] = leftCh            
            
            left += 1
            right -= 1
            
        return "".join(arr)
    

arr = [
    "leetcode",
]
foo = arr[-1]
sol = Solution()
res = sol.reverseVowels(foo)
print(res)