from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        word_map = defaultdict(list)

        for word in strs:
            arr = [0] * 26
            for ch in word:
                ch_index = ord(ch) - ord('a')
                arr[ch_index] += 1
            
            arr_tuple = tuple(arr)
            word_map[arr_tuple].append(word)
    
        return word_map.values()
    

arr = [
    ["", ""],
    ["eat","tea","tan","ate","nat","bat"],
]
foo = arr[-1]
sol = Solution()
res = sol.groupAnagrams(foo)
print(res)
