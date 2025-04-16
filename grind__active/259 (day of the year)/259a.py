# https://leetcode.com/problems/day-of-the-year/description/

class Solution:
    def dayOfYear(self, date: str) -> int:
        pass
        # to know the day of the year
        # the calculation is `numberOfDaysInPreviousMonths + currDay`
        hyphen = '-'
        year, month, days = [int(x) for x in date.split(hyphen)]
        
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        res = days
        if month - 1 > 0:
            res += sum(x for x in month_days[ : month - 1])
        
        # need to be weary of leap years too
        if self.is_leap_year(year) and month > 2:
            # print('is leap year')
            res += 1
            
        return res
            
    
    def is_leap_year(self, year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        
        return year % 4 == 0
    
arr = [
    "2019-01-09",
    "2019-02-10",
    "2004-03-01",
    "2016-02-09",
    "2000-01-31",
]
foo = arr[-1]
sol = Solution()
res = sol.dayOfYear(foo)
print(res)