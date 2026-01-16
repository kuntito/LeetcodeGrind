# https://leetcode.com/problems/valid-parentheses/description/

# given a string containing the characters
#  ( , ) , { , } , [ , ]
# we want to determine if the input string is valid..

# that is, every opening parentheses has a corresponding closing one..
# in the valid order i.e. ')(' has a closing and an opening, but the order is not valid..

# way i know to address is this is to focus on the closing parentheses..
# since every closing must be preceeded by an opening one..
# i'd track all the opens in an array
# once i hit a close, i check the last element in the array..

# if it's an open, i pop it from the array, it's important i pop it
# this signifies that, that pair has been addressed..
# what would be left in the array would be the opens, whose closes i haven't found..

# an edge case would be '('
# for this .. i'd append to the array but never close it..

# in essence, i know, every pair is valid if the tracking array is empty..
# how do you track opens and closes..

# for each close, i want to know it's open.. so a map, a dictionary would suffice
# closes to opens
# okay, but how do you know to append the opens..

# the opens are the chars not in the dict

class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        
        for ch in s:
            if ch not in mapping:
                arr.append(ch)
            elif not arr:
                # we've seen a close but no opens, `arr` is empty
                return False
            else:
                lastOpenCh = arr.pop()
                if lastOpenCh != mapping[ch]:
                    return False
                
        return len(arr) == 0
                