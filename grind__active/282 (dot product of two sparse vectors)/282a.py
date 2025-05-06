# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/

class SparseVector:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.validIndices = set()
        

        for idx, n in enumerate(self.nums):
            if n == 0: continue
            self.validIndices.add(idx)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        uno, dos = self.validIndices, vec.validIndices
        
        commonIndices = uno & dos
        
        res = 0
        for idx in commonIndices:
            numOne, numTwo = self.nums[idx], vec.nums[idx]
            
            res += (numOne * numTwo)
            
        return res

    # what is a sparse vector? a vector that mostly contains zero values
    # what is a vector, an array of numbers
    
    # what is a dotProduct? after staring at the first example, and now, the second example. i can tell the dot product is the result array when you mulitply the respective indices of two vectors
    
    # consider the arrays, `foo` and `bar`, they are both len(2)
    # the dotproduct would be [foo[0] * bar[0], foo[1] * bar[1]]
    
    # it raises the question, does the dot product require both arrays to be the same?
    
    # according to the constraints, yes. it does
    
    # okay so what exactly are we doing? we are to implement the class `SparseVector` that represents the vector, the array of characters but it does more, it provides a method to perform dotproduct operation on another SparseVector class
    
    # and we are to make this efficient
    # given that the goal is dotproduct, it means we can ignore the indices with zeros since this wouldn't give us any benefit
    
    # hence, on creating a sparse vector, we want to know what indices aren't zero, `validIndices`
    # and on dotproduct, we grab the `validIndices` of both arrays
    # and multiply the values there and sum them up
    
    # and we should have our result