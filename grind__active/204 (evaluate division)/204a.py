# https://leetcode.com/problems/evaluate-division/description/

# TODO look at solution
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        pass
    
        # since we can't determine the value of each variable
        # we'd have to be clever
        
        # say you're told:
        # a/b = 2 AND b/c = 3
        
        # to find a/c, you can simply multiply both equations together
        # since it ensures that the `b` would cancel out
        
        # a/b * b/c = 2 * 3 = 6
        
        # in essence when we're given an equation
        # c/d
        # we check if c has any denominators, `Cdenom`
        # where `Cdenom` is the numerator and `d` is it's denominator
        
        # to achieve this, we'd need to map
        # each numerator to it's denominator
        # a numerator can appear more than once, so we could use a pairing
        # `numerator -> set of denominators`
        
        # also keep a hashmap
        # `equation tuple -> result`

        numeratorMap = {}
        equationRes = {}
        
        for eq, res in zip(equations, values):
            num, den = eq
            if num not in numeratorMap:
                numeratorMap[num] = set()
                
            numeratorMap[num].add(den)
            equationRes[(num, den)] = res
            

        arr = []
        for q in queries:
            # print(q)
            res = -1
            
            qNum, qDen = q
            # if the pair already exists, simply grab the results
            qPair = (qNum, qDen)
            if qPair in equationRes:
                res = equationRes[qPair]
            elif (qDen, qNum) in equationRes:
                reverseRes = equationRes[(qDen, qNum)]
                res = 1/reverseRes
                qNum, qDen = qDen, qNum
            elif qNum in numeratorMap:        
                # run through all the denominators of `qNum`
                for potentailDen in numeratorMap[qNum]:
                    # if `potentialDen` exists as a numerator
                    # with `qDen` as a denominator, we have our result
                    if potentailDen not in numeratorMap:
                        continue
                    
                    if qDen in numeratorMap[potentailDen]:
                        leftEq = (qNum, potentailDen)
                        rightEq = (potentailDen, qDen)
                        res = equationRes[leftEq] * equationRes[rightEq]
                        break
            
            arr.append(res)
            if res != -1:
                equationRes[(qNum, qDen)] = res
                numeratorMap[qNum].add(qDen)
            # print(equationRes)            
        return arr
                
            

arr = [
    [
        [["a","b"],["b","c"]],
        [2.0,3.0],
        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    ],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.calcEquation(foo, bar, baz)
print(res)
        
        
        