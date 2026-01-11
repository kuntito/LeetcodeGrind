# https://leetcode.com/problems/meeting-scheduler/description/


class Solution:
    def minAvailableDuration(
        self, slots1: list[list[int]], slots2: list[list[int]], duration: int
    ) -> list[int]:
        pass
        # what is this asking? we are to implement a function that takes three arguments, 2d array of integers and a integer, the function returns an array of integers

        # the 2d arrays are, `slots1` and `slots2`, it represents the available time slots for two people, who meet at a particular time `duration`

        # we are to find the earliest time slot where those two people can have the meeting with time `duration`

        # the elements of each slot is [start, end] representing the time slot for each person. i'd say we sort both slots based on start time

        # then compare the start times of both slots till we find a suitable one.

        # i'm sorting in reverse so i can O(1) access the earliest time slot in both arrays
        slots1.sort(reverse=True)
        slots2.sort(reverse=True)

        # the idea here is i compare the topmost two time slots
        # are they long enough to accomodate the meeting with said duration, if yes you have your result

        # return [startTime, startTime + duration]

        # if not, pop both time slots

        # what if only one time slot is suitable?
        # pop the unsuitable one, and ball

        # what if both time slots are unsuitable, pop both
        # do these while there's values in both slots

        while slots1 and slots2:
            while slots1 and (slots1[-1][1] - slots1[-1][0]) < duration:
                slots1.pop()

            while slots2 and (slots2[-1][1] - slots2[-1][0]) < duration:
                slots2.pop()

            # at this points the only slots in the arrays are valid slots
            if slots1 and slots2:
                # we need to see if the intersection of the topmost slots at this position  allow for a meeting of duration?
                # if yes, when would the meeting be? if not, what do we do?

                # [20, 30] and [30, 40]
                # consider these, in this case we have two valid time slots for duration of five but it don't work
                overlap = self.grabOverlap(slots1[-1], slots2[-1])

                if overlap >= duration:
                    s1, e1 = slots1[-1]
                    s2, e2 = slots2[-1]

                    s = max(s1, s2)
                    return [s, s + duration]
                else:
                    if slots1[-1][0] < slots2[-1][0]:
                        slots1.pop()
                    else:
                        slots2.pop()

                # so what do we do, we pop the one with the lesser time and repeat the loop

        return []

    def grabOverlap(self, valOne, valTwo):
        # how do you grab the overlap
        # the overlap would be the earliest end time minus the latest start time

        s1, e1 = valOne
        s2, e2 = valTwo

        earliestEnd = min(e1, e2)
        latestStart = max(s1, s2)

        return earliestEnd - latestStart


arr = [
    [[[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8],
    [[[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12],
]

foo, bar, baz = arr[-1]
sol = Solution()
res = sol.minAvailableDuration(foo, bar, baz)
print(res)
