# https://leetcode.com/problems/valid-palindrome-ii/description/

# i'm given a string, `s`, 
# and want to find out if it can be a palindrome after deleting at most one character..
# what's a palindrome.. a word that reads the same forward and backward..

# deleting at most one character means, we might not delete any character..
# well, yes, but what does this mean..

# how do we implement this?
# how would you normally track a palindrome..
# two pointers, two pointers at the extreme ends of the string..

# i compare the characters at said pointers, if they match,
# i move the pointers one step towards each other, to check the next set of characters
# if at any point they don't match, i return False..

# i keep doing this while the left pointer is less than the right pointer..
# so what would you need to change to accomodate the deletion..

# it would mean, i can permit one failed match
# consider the string, "abca"

# two pointers, `left` and `right` are initialized at extreme ends
# left = a
# right = a

# they match..
# so i move the pointers one step closer..

# now,
# left = b
# right = c

# they are no longer equal but i can permit this..
# since..it's the first one..

# so what happens next..
# i can't move both pointers towards each other..
# why not, they don't match, the point of the movement was..

# "okay, these two values match, let's consider the next two"
# but now, they don't match. what can i do?

# well, i could move either one of the pointers forward..
# in this example, it wouldn't matter which one i moved forward..
# but i most certainly know, there's ones where it would..

# in essence, i'd have to explore both situations..
# sounding like recursion already..

# i'd need a function that checks palindrome..
# with  two starting arguments..
# `left` and `right`, and the string, `s`
# and a flag to indicate if i've deleted at most one character...

# so the loop would be
# while left < right
#   if the characters match, move pointers one step towards each other
#   if chars don't match, two scenarios:
#       have i deleted one char, { flag handles this}, if i have, return False
#       if i haven't deleted any char, start two recursive calls,
#           one where i move left forward, keep right the same
#           one where i move right backward, keep left the same
# return whichever one is True..
# can i memoize here..
# possibly, since, at every point, i'm doing the same thing..
# the memo key would be (left, right, deletedFlag)
# i don't know if it's overkill for this question..

# i'd solve it without then see if LC complains
# it worked.. without memo..

# also, i missed the return True.. for after the iteration finished..
# so the first submission failed..

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        isDeletedOneChar = False
        
        return self.explore(left, right, s, isDeletedOneChar)
    
    def explore(self, left, right, chars, isDeletedOneChar):
        while left < right:
            leftCh = chars[left]
            rightCh = chars[right]
            
            if leftCh == rightCh:
                left += 1
                right -= 1
            elif isDeletedOneChar:
                return False
            else:
                return self.explore(left + 1, right, chars, True) or self.explore(left, right - 1, chars, True)
            
        return True
            