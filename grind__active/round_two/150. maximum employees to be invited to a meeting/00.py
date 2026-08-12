from typing import List


class Solution:
    def maximumInvitations(
        self,
        favorite: List[int]
    ) -> int:
        pass
        # i sit a person down
        # sit down their favorite.
        # the favorite becomes the person.
        # i sit down their favorite.
        # and keep going.
        
        # then pick the next person.
        # and how would you start this?
        # well, for each person,
        # i need to know their favorites.
        # you do.
        
        # okay, where to store the arrangement.
        # do you need a place?
        # the people are numbered according to indices
        # you'd have an array, `table`, same size as `favorite`
        # this way you know who you've sat.
        
        # nah, this wouldn't work.
        # the table can't be the same -
        # same what?
        # the first chair in the table is the empty chair.
        # next best place to place a person.
        
        # but the table shrinks your reasoning.
        # you only need a structure.
        # to know, who's on the table
        # who's next to them, left and right
        # and build on that.
        
        # so, what?
        # a hashmap
        # yes, each person in an entry
        # pointing to an array.
        # a 2-item array
        # [leftPerson, rightPerson]
        
        # and the length of the hashmap is the number of people sat.
        
        self.hashMapTable = {}
        for person, personFav in enumerate(favorite):

            # now, to sit their fav.
            # i'd check to see if their fav is on the table.
            # if their fav is, can they be sat next to them.
            # if not...
            
            # okay, the fav determines if the person can be sat on a table.
            # so, i'm checking for fav first.
            # if fav on table, can person be sat next to them?
            # if yes, sit person.
            # if not, don't sit person.
            
            # and repeating this'd yield a result?
            # well, yes.
            # doesn't mean it'd be correct.
            
            # so, two scenarios
            if personFav in self.hashMapTable[personFav]:
                leftSlot, rightSlot = self.hashMapTable[personFav]
                # whichever slot is vacant, place a person there.
                # how do i know which is the better slot?
                # try both.
            else:
                # and here? if the persons fav isn't on the table, it means
                # i can add them both.
                self.addPerson(person)
                self.addPerson(personFav)
                
                # now is it better to sit them as
                # `person-personFav` or `personFav-person`
                # well, explore both.
                
                # TODO review approach.
                # so far, you want to explore every possibility
                # then track the largest number sat
                # and return that.
                
                # you found out,
                # the person's fav decides whether the person can be sat at the table.
                # so, for each person you want to place
                # the question is, is their fav on the table.
                
                # if yes, can they be sat next to them?
                # if yes, sit them, if there's more than one place they can sit next to fav
                # explore both
                
                # now, if their fav wasn't on the table to begin with
                # then person and fav can be sat together.
                # however, do you sit them as A-B or B-A
                # explore both.
                
                # that's the recursive approach.
                # at each point, there's someone you want to place.
                # and these are the questions you'd ask for each person.
                
                # and how do you know the next person to pick?
                # you could have an array of participants.
                # or a set, a set is best, you can remove and add at will.
                
                # so you want to take out anyone from the set.
                # see, if you can sit them.
                # if you can't sit them, keep them out the set
                # and see if you can sit the next person.
                # a set might be overkill.
                # an array might just work.
                
                # keeping popping till you run out of people.
                # sometimes, you sit someone without popping cause they're somebody's fav.
                # at which point, you can track those people
                # so, when you do pop them
                # you know to ignore them.
        
        
    def addPerson(self, person):
        if person in self.hashMapTable:
            raise Exception("person already on table")
        
        self.hashMapTable[person] = [None, None]
        
        
    

        
        
                