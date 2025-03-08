# https://leetcode.com/problems/open-the-lock/description/

# https://neetcode.io/solutions/open-the-lock
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        pass
        arr = [
            "0000"
        ]
        
        count = 0
        seen = set(deadends)
        if "0000" in deadends:
            return -1
        # you'd have to convert the combinations to string to check for deadends
        while arr:
            tmp = []
            for comb in arr:
                if comb == target:
                    return count
                seen.add(comb)
                
                comb_int = [int(d) for d in comb]
                newCombs = self.get_new_combinations(comb_int, seen)
                tmp.extend(newCombs)
            arr = tmp
            count += 1
            
        return -1

    def get_new_combinations(self, comb, seen):
        pass
        res = []
        for idx, dig in enumerate(comb):
            clone = comb[::]
            for newPos in self.get_digits(int(dig)):
                clone[idx] = newPos
                newComb = "".join(str(d) for d in clone)
                if newComb in seen:
                    continue
                seen.add(newComb)
                
                res.append(newComb)
                
        return res
    
    def get_digits(self, dial):
        # since each dial can go from 0 - 9, (10 distinct values)
        # we can either turn the dial forward
        # or backward
        
        # for simplicity sake
        # do dial + 1 and dial + 9
        # and mod the results by 10
        # this would simulate turning forward and backward
        
        posOne = (dial + 1) % 10
        posTwo = (dial + 9) % 10
        
        return posOne, posTwo
    
arr = [
    [["0201","0101","0102","1212","2002"], "0202"],
    [["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"],
    [["0000"], "8888"]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.openLock(foo, bar)

print(res)