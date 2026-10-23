from typing import List


class Solution:
    def putMarbles(
        self,
        weights: List[int],
        k: int
    ) -> int:
        # how do i explore the different ways of filling a bag?
        # well, what are the rules?
        
        # first, no bag is empty.
        # the marbles in a bag must be consecutive.
        # p.s. they're lined up in an array.
        
        # okay, so it's really
        # how many different subarray combinations can you get.
        # well, now i'm talking array.
        
        # it's a line or marbles.
        # i have k bags.
        
        # how many different ways can i fill the bags
        # i don't really need the different ways, 
    
        # i need two ways.
        # one with the highest score.
        # and one with the lowest score.
        
        # and how would you get that?
        # let's obtain every way first.
        # then see how to optimize.
        
        # you take it sequential
        # for each bag, explore the different marbles it can take.
        # when done with all the bags, find score.
        # update minScore and maxScore.
        
        # all said and done, return maxScore - minScore.
        
        bagsLeft = k
        curIdx = 0
        self.marbleWeights = weights
        self.dim = len(weights)
        
        self.minScore = float("inf")
        self.maxScore = float("-inf")
        
        distribution = []        
        self.explore(
            bagsLeft,
            curIdx,
            distribution,
        )
        
        return self.maxScore - self.minScore
    
    
    def calc_distribution(self, distribution):
        score = sum(distribution)
        # print(distribution)
        if score < self.minScore:
            self.minScore = score
            
        if score > self.maxScore:
            self.maxScore = score
            
    
    def explore(
        self,
        bagsLeft,
        curIdx,
        distribution,
    ):
        if bagsLeft == 0:
            if curIdx == self.dim:
                self.calc_distribution(distribution)            
            return
        
        
        # what is each bag doing?
        # taking every digit it can take
        # and seeing what happens.
        
        # how do i know every digit it can take?
        # do i need to?
        
        # a bag takes one marble, sees what happens.
        # records that.
        # well, what if i picked two marbles, sees what happens
        # and so on..
        
        firstInBag = None
        lastInBag = None
        for idx in range(curIdx, self.dim):
            marbleWeight = self.marbleWeights[idx]
            
            if firstInBag is None:
                firstInBag = marbleWeight
                
            lastInBag = marbleWeight
                
            distribution.append(
                firstInBag + lastInBag
            )
            
            self.explore(
                bagsLeft - 1,
                idx + 1,
                distribution
            )
            
            distribution.pop()
            
            
arr = [
    [
        [1,3,5,1],
        2,
    ],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.putMarbles(foo, bar)
print(res)