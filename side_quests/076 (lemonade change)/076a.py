# https://leetcode.com/problems/lemonade-change/description/

# TODO https://neetcode.io/solutions/lemonade-change
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        pass
        # declare a till variable that stores each note and it's frequency
        till = {}
        
        # iterate through each bill
        for b in bills:
            till[b] = till.get(b, 0) + 1
            
            # determine if the customer needs change, `change = bills[i] - 5`
            change = b - 5
                            
            # if change > 0, can you give them change from the bills you have
            if change > 0:
                if not self.get_change(change, till):
                    return False
            # if no, return False
        
        # return True at the end of iteration 
        return True
    
    def get_change(self, amount, till):
        tenner, fiver = 10, 5
        while amount:
            if amount >= tenner and tenner in till and till[tenner]:
                till[tenner] -= 1
                amount -= tenner
            elif amount >= fiver and fiver in till and till[fiver]:
                till[fiver] -= 1
                amount -= fiver
            else:
                return False
        
        return True
    
    
arr = [
    [5,5,5,10,20],
    [5,5,10,10,20],
    [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5],
]
foo = arr[-1]
sol = Solution()
res = sol.lemonadeChange(foo)

print(res)