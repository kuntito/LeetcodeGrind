# https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass
        # find the indices longest common subsequence of `word2` in `word1`
        rows = len(word2)
        cols = len(word1)
        
        matrix = [[(0, None) for _ in range(cols)] for _ in range(rows)]
        for ri in range(rows):
            chOne = word2[ri]
            for ci in range(cols):
                chTwo = word1[ci]
                
                if chOne == chTwo:
                    topLeft = matrix[ri-1][ci-1] if ri-1 >= 0 and ci-1 >= 0 else (0, None)
                    
                    count, indices = topLeft
                    
                    count += 1
                    if indices is None:
                        indices = [ci, ci+1]
                    else:
                        indices[1] = ci + 1
                    matrix[ri][ci] = (count, indices)
                else:
                    above = matrix[ri-1][ci] if ri - 1 >= 0 else (0, None)
                    before = matrix[ri][ci - 1] if ci - 1 >= 0 else (0, None)
                    
                    if above[0] > before[0]:
                        matrix[ri][ci] = above
                    else:
                        matrix[ri][ci] = before
                
        s, e = matrix[-1][-1][1]
        print(word1[s:e])
    
    def get_LIS_indices(self, one, two):
        pass
    

arr = [
    ["", "a"],
    ["horse", "ros"],
    ["intention", "execution"], #TODO wetin i don write?
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minDistance(foo, bar)
print(res)
        
        
        
        