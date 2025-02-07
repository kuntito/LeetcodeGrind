# https://leetcode.com/problems/asteroid-collision/description/

# TODO rewrite, you misread the question
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        pass
        # create an array, `res`
        
    
        dim = len(asteroids)
        res = []
        idx = dim - 1
        
        while idx >= 0:
            val = asteroids[idx]
            if val > 0:
                res.append(val)
                
            if val < 0:
                if idx - 1 >= 0 and asteroids[idx - 1] > 0:
                    collision = self.collide(idx-1, idx, asteroids)
                    asteroids[idx - 1] = collision
                    
                    if collision is None:
                        idx -= 1
                    elif collision > 0:
                        res.append(collision)
                        idx -= 1
                else:
                    res.append(val)
                    
            idx -= 1
                    
        return res[::-1]
    
    
    def collide(self, posIdx, negIdx, arr):
        posNum, negNum = arr[posIdx], arr[negIdx]
        
        negAbs = abs(negNum)
        if posNum == negAbs:
            return None
        
        return posNum if posNum > negAbs else negNum
        
        
arr = [
    [8, -8],
    [5, 10, -5],
    [10,2,-5],
    [-2,-1,1,2],
    [-2,2,-1,-2],
]
foo = arr[-1]
sol = Solution()
res = sol.asteroidCollision(foo)
print(res)