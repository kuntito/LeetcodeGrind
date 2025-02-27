# https://leetcode.com/problems/matchsticks-to-square/description/

from collections import Counter
class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        pass
    
        # the sum of matchsticks divided by 4 determines the length of each side
        # if the sum is not wholly divisible by 4, return False
        
        total = sum(matchsticks)
        if total % 4: return False
        
        side_len = total // 4
        
        # create a hashmap of elements
        elements = Counter(matchsticks)
        
        # create an array of unique elements
        array = list(elements.keys())
        # sort the array
        array.sort()
        
        # starting from the largest
        # decrement it from the hashmap, if it's exhausted remove it from the hashmap
        while array and array[-1] in elements:
            largest = array[-1]
            complement = side_len - largest
            self.decrement_and_clean_up(largest, elements)
            
            if complement == 0:
                continue
            
            while complement > 0:
                # TODO
                # the question here is can you make up `complement`
                # with the remaining elements
                # if yes, decrement and clean up
                pass
            
            
        return not elements
            
            
    def decrement_and_clean_up(self, elem, counter):
        if elem in counter:        
            counter[elem] -= 1
            
            # clean up
            if counter[elem] == 0:
                del counter[elem]


arr = [
    [1,1,2,2,2],
]
foo = arr[-1]
sol = Solution()
res = sol.makesquare(foo)
print(res)