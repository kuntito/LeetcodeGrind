# https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        pass
        people.sort()
        
        left, right = 0, len(people) - 1
        
        count = 0
        while left <= right:
            total = people[left] + people[right] if left < right else people[left]
            if total <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            
            count += 1
            

            
        return count