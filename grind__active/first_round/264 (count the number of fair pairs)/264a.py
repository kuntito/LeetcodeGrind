# https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

from collections import Counter
class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        pass
        # a pair is fair if the indices are different and are within the inclusive bounds of `lower` and `upper`
        
        # looks like a sorting then combination problem
        # sort the array
        # use two pointers, `si` and `ei` to for the start index and end index
        
        # move them until the sum of their values are less than `upper`
        # at which point, determine the number of elements between them
        # and find out how many different ways you can select two elements from them
        
        # not really...
        # consider: [1, 2, 3, 3, 5], where upper = 5
        # at this point, we'd finna move the end pointer
        # since `5` combined with the smallest number `1` is greater than the range
        
        # now, we'd have
        # [1, 2, 3, 3]
        
        # (1, 3) are valid pairs
        # so we move out the bigger one, right pointer
        # then we'd find another (1, 3)
        # move out the bigger pointer
        # then have (1, 2) and everybody goes home
        
        # [0, 1, 4, 4, 5, 7]
        
        # (1, 5)
        # (1, 4)
        # (1, 4)
        
        # which would be wrong since (0, 1), (0, 4), (0, 5)
        # are all valid pairs
        
        # does this mean we'd need a bruteforce approach??
        # might need one and might need caching?
        
        # thing is for `0`, there's `n` elements that can pair up with it to be within range
        # moving left to right, for each unique element, we determine it's number of complements
        # and update the count as we go along
        
        
        
        
        # create a list of unique numbers in `nums`
        # sort them
        
        
        # go through each number in the list
        # for each number
        # check subsequent numbers if adding them makes a valid range
        
        self.lower = lower
        self.upper = upper
        num_map = Counter(nums)
        
        uniques = sorted(list(num_map))
        # print(uniques)
        
        res = 0
        dim = len(uniques)
        for idxOne in range(dim):
            numOne = uniques[idxOne]
                        
            # for duplicates of `numOne`
            if self.is_in_range(numOne, numOne):
                res += num_map[numOne] - 1
            for idxTwo in range(idxOne + 1, dim):
                numTwo = uniques[idxTwo]
                if self.is_in_range(numOne, numTwo):
                    res += num_map[numTwo]
                    
                    
        return res
        

        
    def is_in_range(self, numOne, numTwo):
        total = numOne + numTwo
        return self.lower <= total <= self.upper
        
arr = [
    [[0,1,7,4,4,5], 3, 6],
    [[1,7,9,2,5], 11, 11],
    [[0, 0, 0, 0, 0, 0], 0, 0],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.countFairPairs(foo, bar, baz)
print(res)