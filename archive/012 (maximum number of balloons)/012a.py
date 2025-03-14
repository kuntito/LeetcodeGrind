# https://leetcode.com/problems/maximum-number-of-balloons/description/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_map = {}

        target = 'balloon'
        for ch in text:
            if ch in target:
                char_map[ch] = char_map.get(ch, 0) + 1

        
        count = 0
        while self.remove_target(char_map, target):
            count += 1
        return count
    

    def remove_target(self, char_map, target):
        for ch in target:
            if ch in char_map:
                char_map[ch] -= 1
                if char_map[ch] == 0:
                    del char_map[ch]
            else:
                return False

        return True


arr = [
    "loonbalxballpoon",
    "nlaebolko",
    "balon",
]
foo = arr[-1]
sol = Solution()
res = sol.maxNumberOfBalloons(foo)
print(res)
