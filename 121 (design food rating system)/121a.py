# https://leetcode.com/problems/design-a-food-rating-system/description/

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        pass
    
        # hashmap of cuisines
        # key => cusine
        # value => max heap (- min heap)
        
        # hashmap for foods => rating
        # list for rating removal, `removal_list`
        
        # when you change the rating

        # TODO how do you know what food is in what cuisine?

        # determine what the existing rating is
        # store it in the list for removal
        
        # then simply push (-new_rating, food) to the heap
        
        # when you need the highest rated
        # determine what the highest rating for the cuisine is
        # i.e. -10
        # iteratively pop the top value from the heap if it's value is == `-10`
        
        # take not to ignore any value in `removal_list`
        # once all candidates are retrieved, determine the lexicographically smaller string and return it

    def changeRating(self, food: str, newRating: int) -> None:
        pass

    def highestRated(self, cuisine: str) -> str:
        pass


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)