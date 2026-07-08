class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass
        # my first window, is size 3.
        # how do i represent a window?
        # indices.
        # left and current?
        # start and current
        # winStart and winEnd.
        
        # then how do i represent gaps?
        # a gap is the absence of characters
        # well, it's the absence of one particular character.
        # what character is that, the most popular character in the window.
        # and if there's several? pick anyone.
        
        # in other words,
        # i need to know what characters are popular within the window?
        # i need to track the count of characters.
        # then also track the most popular one.
        
        # this lends itself nicely to a hashmap
        # i can track the most popular at add time.
        # the hashmap, also lets me reduce the count
        # when shrinking the window?
        
        # but during shrinking
        # how do you maintain the most popular count?
        # unless, you track the order of who was popular at each point
        # you don't know.
        
        # again, my past knowledge is interfering.
        # do i need to update the most popular when shrinking my window?
        # well, no.. because, i'm optimizing for the most popular i can find
        # and since, i'm shrinking the window,
        # any character that takes the most popular crown
        # is definitely less popular than what came before it
        # and by definition, irrelevant.
        
        # i only care about the most popular characters that increase the window size
        # however, not sure this would fly for a bottom up approach.
        # i'd probably have to track the most popular at all times
        # then explain why it's irrelevant.
        
        # but for the sake of just testing, let's go.
        
        
        windowContent = {}
        winStart = 0
        winEnd = 0
        
        dim = len(s)
        
        # at first, my longest streak is `0`
        longestStreak = 0
        gapCount = 0
        mostPopularCount = 0
        
        while winEnd < dim:
            currChar = s[winEnd]
            
            # i want to add the char to the window
            # but first check if i should shrink the window
            # what's the check for shrink, 
            # if gap count exceeds k
            
            while gapCount > k:
                # how do i shrink..
                # remove the char at `winStart`
                # update mostPopular's count
                # recalculate the gap
                
                # tbf, i don't even need the `longestStreak` argument.
                # i just need to know the mostPopular count while gap <= k
                self.decrementCharCount(
                    windowContent,
                    s[winStart]
                )
                
                
                
            
            winEnd += 1
            
            
    def decrementCharCount(self, hashMap, ch):
        if ch not in hashMap:
            raise Exception(f"{ch} is not in hashmap")
        
        hashMap[ch] -= 1
        if hashMap[ch] == 0:
            del hashMap[ch]
        