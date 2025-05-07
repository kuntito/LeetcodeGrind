# https://leetcode.com/problems/find-the-celebrity/description/
# # The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

from collections import defaultdict


def knows(a, b):
    return True

# TODO the assumption here is wrong, `unknowns` is the opposite of what we want, the celebrity is the person know by all
# rewrite! FIXME
class Solution:
    def findCelebrity(self, n: int) -> int:
        pass
        # why will a celebrity go to a party when doesn't know anybody?
        
        # the first thing we want to know is who knows who, it's sounding like a graph problem. we need a graph of all the people
        
        # in essence, a n square loop that checks if everyone knows everyone
        
        # say you had the graph, what do you do next?
        
        # i'd say creating the graph reveals the celebrity, if they exist
        # the idea is everyone in the party is labelled 0 to n-1
        # we can place 0 to n-1 in a set
        
        # and create the graph
        # in creating the graph, we remove every known person from the set
        
        # wrong, we are looking for a celebrity, by definition, they don't know anyone in the room
        # so all their `knows` should return False
        
        # if we explore everyone against everyone else, if `knows` ever returns True, then we exclude them from the candidates
        
        # yes, but it's possible to not know everyone and yet nobody knows you, you could be the quintessential loner
        
        # what if we create a reverse relationship in the graph
        # such that for each person, we know all the people they know
        
        # the set helps us know the candidates for celebrity.
        
        # might have to start over
        # we want to create a graph, where each persons neighbours are the people that know them
        
        # while creating this graph, we want to take note of people that are unknown
        
        # whoever is in this set is a candidate for celebrity
        # we'd then explore everyone in this set for their followers
        
        # if they have `n-2` followers, they are the celebrity
        # if nobody does, there's no celebrity so we return -1
        
        unknowns = set(range(n))
        self.everybody = n
        graph = self.createGraph(unknowns)
        
        print(unknowns)
        
    def createGraph(self, unknowns):
        pass
        graph = defaultdict(set)
        for person in range(self.everybody):
            for anotherPerson in range(self.everybody):
                if person == anotherPerson: continue
                
                if knows(person, anotherPerson):
                    if anotherPerson in unknowns:
                        unknowns.remove(anotherPerson)
                    graph[anotherPerson].add(person)
                    
        return graph
        
        
