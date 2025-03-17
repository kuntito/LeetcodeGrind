# https://leetcode.com/problems/reorder-data-in-log-files/description/

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        pass
    
        # separate digit logs from letter logs
        # perform lexographical sort on letter logs
        # keep digit logs as is
        # combine them as in `letter logs + digit logs`
        
        letterLogs, digitLogs = [], []
        
        for lg in logs:
            if lg[-1].isalpha():
                letterLogs.append(lg)
            else:
                digitLogs.append(lg)
                

        sortedLetterLogs = self.lexiSort(letterLogs)
        
        sortedLetterLogs.extend(digitLogs)
        return sortedLetterLogs
    
    def lexiSort(self, letterLogs):
        pass
        # create intermediary array
        # each item is the [identifier, data]
        
        space = " "
        interm = []
        for lg in letterLogs:
            idfr, data = lg.split(space, 1)
            interm.append((idfr, data))
  
        interm.sort(key=lambda a: (a[1], a[0]))  
  
        
        res = [a + space + b for a, b in interm]
        # print(res)
        return res

        
arr = [
    ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
    ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"],
]
foo = arr[-1]
sol = Solution()
res = sol.reorderLogFiles(foo)
print(res)
