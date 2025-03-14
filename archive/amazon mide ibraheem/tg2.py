# multiply all the numbers by the factor, save the res in a new array
# divide all the numbers by the factor, save the res in a new array

# perform kadane on both arrays
# return the largest result

import math
def solution(ratings, impactFactor):
    
    amplified_ratings = [r * impactFactor for r in ratings]
    segAmp = kadane(amplified_ratings)
    if impactFactor == 1:
        return segAmp
    
    
    adjusted_ratings = []
    for r in ratings:
        r /= impactFactor
        # if positive, `floor`
        if r > 0:
            r = math.floor(r)
        else:
            # use `ceil`
            r = math.ceil(r)
        adjusted_ratings.append(r)
        
    segAdj = kadane(adjusted_ratings)
        
    print(amplified_ratings)
    return max(segAmp, segAdj)
        
def kadane(nums):
    maxSum = nums[0]
    tmp = 0
    
    for n in nums:
        if tmp < 0:
            tmp = 0
            
        tmp += n
        
        maxSum = max(maxSum, tmp)
        
    return maxSum
        

arr = [
    [[-2, 3, -3, -1], 1],
    [[4, -5, 5, -7, 1], 2],
    [[5, -3, -3, 2, 4], 2],
]
foo, bar = arr[-1]
res = solution(foo, bar)
print(res)
