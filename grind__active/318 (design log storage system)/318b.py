# https://leetcode.com/problems/design-log-storage-system/
from typing import List
from datetime import datetime, timezone


class LogSystem:
    def __init__(self):
        self.stamps = []

    def put(self, id: int, timestamp: str) -> None:
        numStamp = self.convertToNum(timestamp)
        self.stamps.append((id, numStamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        start = self.makeGranular(start, granularity)
        # end = self.makeGranular(end, granularity)

        numStart = self.convertToNum(start)
        numEnd = self.convertToNum(end)

        self.stamps.sort(key=lambda x: x[1])

        res = []
        for idx, ts in self.stamps:
            if ts > numEnd:
                break

            if ts >= numStart:
                res.append(idx)

        print(res)
        return res


    def makeGranular(self, timestamp, granularity):
        granMap = {
            "Year": 0,  # Zero from Month (index 1) onwards
            "Month": 1,  # Zero from Day (index 2) onwards
            "Day": 2,  # Zero from Hour (index 3) onwards
            "Hour": 3,  # Zero from Minute (index 4) onwards
            "Minute": 4,  # Zero from Second (index 5) onwards
            "Second": 5,  # No zeroing (index 6 is out of bounds)
        }

        arr = timestamp.split(":")
        startIdx = granMap[granularity]

        # Zero all components starting from startIdx
        for idx in range(startIdx + 1, len(arr)):
            a = "00"
            if idx in (1, 2):
                a = "01"
            arr[idx] = a

        return ":".join(arr)

    def convertToNum(self, timestamp: str):
        # Parse the timestamp into a datetime object
        print(timestamp)
        dt = datetime.strptime(timestamp, r"%Y:%m:%d:%H:%M:%S")
        # Set epoch (e.g., Unix epoch 1970-01-01 00:00:00 UTC)
        epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
        # Ensure the datetime is timezone-aware (adjust as needed)
        dt = dt.replace(tzinfo=timezone.utc)
        # Calculate the difference
        delta = dt - epoch
        # Return total seconds
        return int(delta.total_seconds())
        # parts = [int(x) for x in timestamp.split(":")]

        # # i need to convert each element in `parts`
        # # to their equivalents in seconds

        # # then return the sum of everything

        # secondsPerMinute = 60

        # minutesPerHour = 60
        # secondsPerHour = secondsPerMinute * minutesPerHour

        # hoursPerDay = 24
        # secondsPerDay = secondsPerHour * hoursPerDay

        # isLeap = self.isLeapYear(parts[0])
        # daysInMonth = self.getDaysInMonth(parts[1], isLeap)
        # secondsPerMonth = daysInMonth * secondsPerDay

        # daysInYear = 365 + (1 if isLeap else 0)
        # secondsPerYear = daysInYear * secondsPerDay

        # # year
        # parts[0] *= secondsPerYear

        # # month
        # parts[1] *= secondsPerMonth

        # # day
        # parts[2] *= secondsPerDay

        # # hour
        # parts[3] *= secondsPerHour

        # # minute
        # parts[4] *= secondsPerMinute
        # # seconds
        # parts[5]

        # return sum(parts)

    def getDaysInMonth(self, month: int, isLeap: bool):
        # 30 - sep, april, june, november
        # 28/29 february
        # 31
        monthStrMap = {
            0: "jan",
            1: "feb",
            2: "mar",
            3: "apr",
            4: "may",
            5: "jun",
            6: "jul",
            7: "aug",
            8: "sep",
            9: "oct",
            10: "nov",
            11: "dec",
        }

        monthDays = {
            "jan": 31,
            "feb": 28,
            "mar": 31,
            "apr": 30,
            "may": 31,
            "jun": 30,
            "jul": 31,
            "aug": 31,
            "sep": 30,
            "oct": 31,
            "nov": 30,
            "dec": 31,
        }

        monthStr = monthStrMap[month]

        addition = 1 if monthStr == "feb" and isLeap else 0
        return monthDays[monthStr] + addition

    def isLeapYear(self, year: int):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


sol = LogSystem()
sol.put(1, "2017:01:01:23:59:59")
sol.put(2, "2017:01:01:22:59:59")
sol.put(3, "2016:01:01:00:00:00")


sol.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year")
sol.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour")
