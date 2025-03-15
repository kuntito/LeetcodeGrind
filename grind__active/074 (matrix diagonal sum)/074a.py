class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        pass
        dim = len(mat)
        self.dim = dim
        self.mat = mat
        
        has_center = bool(dim % 2)
        
        res = 0
        res += self.exploreDir((0, 0), (1, 1), has_center)
        res += self.exploreDir((0, dim-1), (1, -1), has_center)
        
        if has_center:
            cent = dim//2
            res += mat[cent][cent]
            
        return res
        
        
    def exploreDir(self, origin, diR, has_center):
        pass
        r, c = origin
        inc_r, inc_c = diR
        cent = self.dim//2
        
        res = 0
        while r >= 0 and r < self.dim and c >= 0 and c < self.dim:
            if has_center and r == self.dim//2 and c == self.dim//2:
                r += inc_r
                c += inc_c
                continue
            
            res += self.mat[r][c]
            print(self.mat[r][c])
            
            r += inc_r
            c += inc_c
            
        return res
    
arr = [
    [[1,2,3],
    [4,5,6],
    [7,8,9]],
]

foo = arr[-1]
sol = Solution()
res = sol.diagonalSum(foo)
print(res)