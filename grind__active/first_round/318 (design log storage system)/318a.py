# https://leetcode.com/problems/design-log-storage-system/
from typing import List

# i want to implement a class, `LogSystem`
# the class has three methods, the constructor, `put` and `retrieve`

# the `put` method takes two arguments, an integer `id` and a string `timestamp` and returns `None`

# perhaps, it's better to take a moment to understand the question
# then describe what a solution entails

# we want to implement a system for storing timestamps
# each timestamp is in the format "year:month:day:hour:minute:second" 

# 6 divisions

# storing the timestamp seems easy until we read the requirements
# for the retrieve method

# it takes three string arguments, `start`, `end` and `granularity`
# and returns a list of integers

# `start` and `end` are timestamps, they represent a range of timestamps we want to explore.

# is the range inclusive, the question doesn't say. the example suggests it is. i'd assume the range is inclusive until shown otherwise.

# `granularity` determines how specific we want the ranges to be

# for example, say we've stored these three timestamps:

# [1, "2017:01:01:23:59:59"]
# [2, "2017:01:01:22:59:59"]
# [3, "2016:01:01:00:00:00"]

# and we call the `retrieve` method with the following arguments,
# ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"]

# what would this mean?
# the granularity is "year", does it mean i check every of the six divisions
# and stop and "year"?

# let's examine the result [3, 2, 1]
# these are the ids of all the timestamps we've stored

# it seems i'm on to something with the check every division up until "year"

# how about the next example?
# ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]

# the granularity is "hour"
# if my assumption is right, it means i should check every division up until "hour"
# what does check every division mean?
# let's itemize the `start` and `end` stamps

# Year  2016 2017
# Month 01   01
# Day   01   01
# Hour  01   23
# Min   01   00
# Sec   01   00

# now then, what does a range with hour granularity mean?
# get all years from (2016 - 2017)
# out of those years, get all months from 01-01
# out of those months, get days from 01-01
# out of those days, get hours from 01-23

# and stop there, of the three examples, only [2, 1]
# meet the criteria


class LogSystem:
    def __init__(self):
        pass

    def put(self, id: int, timestamp: str) -> None:
        pass

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        pass
