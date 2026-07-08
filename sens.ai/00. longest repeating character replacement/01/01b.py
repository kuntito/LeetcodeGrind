class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass
        # i'd grow a window from size 1
        # till adding a new character makes the gap exceed k.
        
        # at which point, i remove the leftmost character in the window.
        # keeping the window at it's max size.
        
        # i'd keep an eye out, if i ever find a char
        # that exceeds the most popular so far.
        
        # TODO, i think you're on to something here.
        # but the logic isn't clear.
        
        # what's true, you always want to add characters to the window
        # if mostPopular doesn't increase, and you've hit max gaps before
        # shrink the window by 1, shrink fromt the left.
        # repeat this until you find a window that increases `mostPopular`
        # whichever case, return `mostPopular + k`
                
