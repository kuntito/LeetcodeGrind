# https://leetcode.com/problems/text-justification/

from typing import List

# i'm given a list of words.
# i want to arrange these words into a block of text.

# every line in the block of text 
# has the same number of characters.

# to fill the block of text,
# i'd place each word followed by a space.

# it's possible that i don't have enough words and spaces
# to meet the required character count.

# in that case, i place extra spaces between words
# until the character count is met.

# i continue on every next line till i run out words.
# the last line is different.

# if i don't have enough words to meet the character count.
# i can just fill the rest of the line with spaces.

# and how would this go in code?
# well, i'd take each word and place it on a line.

# i'd keep track of the words on that line to ensure
# i don't exceed the character count.

# if i've gotten to a point where taking another word
# makes me exceed the required character count.

# i add extra spaces between the existing words
# then start a new line.

# i repeat until i exhaust the words.
# i'd also make an exception for the last line.
# where i can just fill the rest of it with space.

# okay, and how exactly are you tracking word count with space
# i'd track the words on each line with an array.

# before adding a new word to the line.
# i want to know if all the existing words plus in-between spaces
# allow for a new word.

# if not, i know i'm done with that line..
# and would use a helper function to determine the spaces i want.

# the helper function would take the array of line words.
# and the required character limit.
# it'd return a string of the line with the necessary spaces.
# i'd append the line to the result array.

# then repeat.

# for the last line..
# how would i know? well it'd be if i'm at the last index.
# i could add a flag to the helper function, `isLastLine`,
# so it treats it different.

# case closed.

# error, i realized i never needed last index in the helper function, `justifyLine`
# i'd included it in the function call, but didn't write it in the function definition.

# i knew i had to remove it but left it in.
# telling myself, it would just be an unused variable.

# that would have been True, if i added it in the function definition
# but i didn't so i created a bug.

# should've removed it the moment i knew i didn't need it.

# error, my function for concatenating the words on the line
# adds space after every word.
# this shouldn't be the case.

# it should only add a space
# after every word except the last word.

# another approach is to iterate over slots..
# this way the loop tells me how many spaces i need.

# but then i'd need a way to track what word in `wordsOnLine` i'm on
# it's best to just keep it as is and note when the last word is.

# this function could definitely be cleaner. TODO rewrite.

# error, i checked last word with `idx + 1 < len(w)`
# it should be length of wordsOnLine not the length of the current word.

# error, i didn't add the check for last word in the right place.
# i'd placed it above the line decrementing extra space as opposed to the line
# adding the space between words.

# error, i didn't account for zero slots.
# overall, this was not the best the attempt.

# i understood the problem, overestimated the need for examining edge cases
# and i blundered it.

# i'd try again.

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        
        line = []
        # i should track the length of the words on a line
        # a counter that accompanies my iteration through words
        # `charCount`
        # for every word, i add len(w) to charCount..
        # if charCount > 0, i add `1` before adding len(w)
        # this accounts for the space..
        
        # so i always know the current charCount on each line
        charCount = 0
        for idx, w in enumerate(words):
            newCharAddition = len(w) + (1 if charCount else 0)
            canTakeNewWord = charCount + newCharAddition <= maxWidth
            if canTakeNewWord:
                charCount += newCharAddition
                line.append(w)
            else:
                res.append(
                    self.justifyLine(
                        line,
                        maxWidth,
                    )
                )
                
                line = [w]
                charCount = len(w)
                
        # the way it's written, the last line never gets into `res`
        # reason being.. i only append a line, the moment i realize the next word
        # wouldn't fit...
        
        # in the case of the last line, 
        # it's either i'd realize the last word wouldn't fit..
        # append the penultimate line
        # the initialize line and charCount to the last word..
        # then the loop ends..
        
        # or i would have been building the last line but it never gets appended
        # because i never found a word that tipped the charCount over the limit.
        
        # in both cases, the loop will end with `line` having at least one word
        # and charCount > 0
        
        # so i should address the last line after the loop ends..
        
        lastLine = " ".join(line)
        if len(lastLine) < maxWidth:
            diff = maxWidth - len(lastLine)
            lastLine += (diff * " ")
            
        res.append(lastLine)
                
        return res


    def justifyLine(self, wordsOnLine, maxWidth):
        pass
        # what am i doing here?
        # i want to place spaces between each word until
        # the length of the entire line is equal to maxWidth.
        
        # how do you determine how many spaces you'd need.
        # well, `maxWidth - sum of the length of words in line..`
        # you could probably get this from charCount..
        # but you'd have to have separated charCountWords and charCountSpaces..
        
        # nonetheless, move on..
        # rewrite with better foresight TODO
        
        # once, i know the number of spaces, i'd need what next?
        # well place the words space at a time.
        
        # the tricky bit is what if i can't divide the space evenly.
        # say i have two spaces with 7 spaces to share.
        
        # i'm told to priortize the spaces on the left.
        # which would mean the first slot gets 4 spaces, the second one get's three.
        
        # but how would i write this in code..
        # say i had three slots with 5 spaces.
        
        # how do i know who gets two spaces and who gets one..
        # well 5 divided by 3 is one.
        
        # so, every body get's at least one..
        # what's the remainder?
        # two.
        
        # so the first two slots get an additional one space.
        
        spacesRequired = maxWidth - sum(len(w) for w in wordsOnLine)
        slots = len(wordsOnLine) - 1
        
        minSpace, extraSpace = divmod(spacesRequired, slots)
        
        space_ch = " "
        res = []
        for idx, w in enumerate(wordsOnLine):
            res.append(w)
            
            if idx + 1 < len(wordsOnLine):
                res.append(
                    space_ch * (minSpace + extraSpace)
                )
            
            if extraSpace > 0:
                extraSpace -= 1
                
        return "".join(res)


arr = [
    [
        ["This", "is", "an", "example", "of", "text", "justification."],
        16,
    ]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.fullJustify(foo, bar)
