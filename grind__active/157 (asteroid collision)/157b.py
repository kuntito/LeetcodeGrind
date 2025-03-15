# https://leetcode.com/problems/asteroid-collision/description/

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        pass
        # keep a stack of elements seen
        # for every negative element seen
        # check if the last stack element is positive
        # if it is, collide them
        
        stack = []
        for n in asteroids:
            while n and n < 0 and stack and stack[-1] > 0:
                numOne = stack.pop()
                n = self.collide(numOne, n)


            if n is not None:
                stack.append(n)
                
        return stack
    
    def collide(self, pos, neg):
        neg_abs = abs(neg)
        
        if pos == neg_abs:
            return None
        elif pos > neg_abs:
            return pos
        
        return neg
            

        
        
arr = [
    [8, -8],
    [-2,-1,1,2],
    [-2,2,-1,-2],
    [5, 10, -5],
    [10,2,-5],
]
foo = arr[-1]
sol = Solution()
res = sol.asteroidCollision(foo)
print(res)