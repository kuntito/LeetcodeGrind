# https://leetcode.com/problems/dota2-senate/description/

# right, there's two parties, `Radiant` and `Dire`
# both parties consist of senators

# and the senate wants to take a vote
# a peculiar vote.
# the voting is such that each senator can do one of two things.

# ban one senator or announce victory.
# banning means a senator from an opposing party cannot vote
# announcing victory is based on the current votes and the amount of senators left

# say the votes are tied and the remaining senators

# REWRITE!!!

# two political parties, 'Radiant' and 'Dire'
# and they want to take a vote.

# the parties consist of senators and each senator can only vote for his party
# given a queue of senators, we want to find out which party would win the votes.

# however, the voting is carried out in a unique manner.
# after casting their vote, each senator can do one of two things:

# ban a senator from the opposing team,

# OR

# announce victory

# banning is simple, it means a senator from the opposing party doesn't get to vote

# announcing victory is based on the votes so far and the senators left in the queue
# say after voting, the current senator who is from 'Radiant', realizes the votes are tied 3-3
# and the remaining senators in the queue are from his party
# he can declare victory

# i think declaring victory would be the tricky part of the code.

# the question is, suppose every senator is smart enough and will play the best strategy for his own party
# which party would win the votes.

# the output should be 'Radiant' or 'Dire'

# the input is a string, `s`, that contains either 'R' or 'D'

# now, what would the optimal strategy look like?
# i imagine banning is always a good strategy if you can't announce a winner
# since it increases the chances of your party winning

# apparently, you can ban senators who have already voted.
# this changes things a bit.

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        pass