# https://leetcode.com/problems/find-the-celebrity/description/

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# what is the question here? we are at a party with `n` people
# each person has a label from `0` to `n-1`

# and among said people, a celebrity might exist. a celebrity is defined as the person that knows no one but is known by everyone

# we want to find this celebrity
# we want to implement a function `findCelebrity` that takes an integer `n` and tells us who the celebrity is

# we're given additional info in the form a function, `knows`
# this function takes two integer arguments i.e. knows(a, b)
# and returns a boolean indicating if `a` knows `b`

# if a celebrity exists, return their label else return -1
def knows(a, b):
    return True

class Solution:
    
    # how would i go about this? for each person, i need to know who they know
    # yes, but how would you find the guy that knows no one but everybody knows
    
    # i can think of a naive approach where i want to determine the guys that know no one first
    # i'd run a n2 loop and call `knows`
    
    # i want to find the labels that finish that loop without knowing anyone
    
    # once i have those guys, i want to know if everyone knows them
    
    def findCelebrity(self, n: int) -> int:
        candidates = []
        
        for i in range(n):
            if self.is_person_candidate(i, n):
                candidates.append(i)
                
        # after determining the candidates, i want to know if they are known by everyone
        # how would this work
        for cand in candidates:
            if self.is_celebrity(cand, n):
                return cand
            
        return -1
    
    def is_celebrity(self, cand, labels):
        return all(knows(l, cand) for l in range(labels))
    
    def is_person_candidate(self, i, n):
        for j in range(n):
            if i == j: continue
            
            if knows(i, j):
                return False
            
        return True