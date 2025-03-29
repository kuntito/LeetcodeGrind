class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = self.createMap(nums)
        
        
        
    def createMap(self, nums):
        # write the breakdown for this function
        hashMap = {}
        
        for idx, n in enumerate(nums):
            if n not in hashMap:
                hashMap[n] = []
            hashMap[n].append(idx)
            
        return hashMap