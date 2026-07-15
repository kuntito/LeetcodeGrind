from typing import List


class Solution:
    def minimumTime(
        self,
        n: int,
        relations: List[List[int]],
        time: List[int]
    ) -> int:
        # for every course, i'd like to know it's pre-requisites
        # a hashmap would suffice.
        
        # once, i have this, i want to pick