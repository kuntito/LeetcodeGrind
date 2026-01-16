# https://leetcode.com/problems/valid-palindrome/

# we're given a string `s` and want to find out if `s` is a palindrome.
# a palindrome is a string that reads the same forward and backward..
# however, there's a catch..

# we're not considering all the characters in `s` for the palindrome check
# we only want to consider alpha numeric characters in our palindrome check
# so the question, in essence is, do the alphanumeric characters in `s`
# form a palindrome..

# how do we tell if it's alpha numeric, i think Python has a method for that.
# `isalnum`, one more thing we don't care about case, 'A' is the same as 'a'

# i'd say two pointers, left and right..
# they move toward each other long as they are the same case insensitive character..
# and how would you address non-alphanumerics..

# a while loop.. the main loop would be while `left < right`
# but within the loop, we'd move left forward if it's current character is non-alpha
# and do the same righ right, we'd move right leftwards until we hit an alpha num..
# but with this logic, it's possible for left to cross right or land on right..
# and we don't do the left < right check within the loop..

# well this is enough reason to do it...
# for all intents, it could be a while True.. loop
# after all the movements, verify the left < right..
# if yes, left += 1, right -= 1

# how would you address '?'
# based on your logic, you'd want to move left forwards..
# it'd go out of bounds..
# okay.. you'd also move right backwards, out of bounds to
# but left > right.. so it wouldn't matter

# slight misstep, if left crosses right i.e. left > right
# that does mean a palindrome exists

# the earlier example of '?' would result in that..
# the question asks to consider all alphanumerics without considering their case..

# in '?', there are None and the string of concern is effectively an empty string ''
# which is a palindrome..

# also, you want to check `left > right` befroe checking leftCh != rightCh
# if you did the character check first and the pointers have crossed, you'd have an index error..

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        dim = len(s)
        
        while True:
            while left < dim and not s[left].isalnum():
                left += 1
                
            while right >= 0 and not s[right].isalnum():
                right -=1
                
                        
            if left > right:
                return True

            leftCh = s[left].lower()
            rightCh = s[right].lower()
            if leftCh != rightCh:
                return False

            
            left += 1
            right -= 1
            
arr = [
    "A man, a plan, a canal: Panama",
    "race  car",
]
foo = arr[-1]
sol = Solution()
res = sol.isPalindrome(foo)
print(res)