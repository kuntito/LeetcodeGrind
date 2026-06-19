import heapq
from typing import List

class Solution:
    def fullBloomFlowers(
        self,
        flowers: List[List[int]],
        people: List[int]
    ) -> List[int]:
        # heapify the people array.
        # heapify the flowers array.
        
        # create the return array.
        # pop the first person.
        
        # compare their arrival time
        # with the flower blooming first.
        
        # if the tip of flower heap
        # already bloomed, pop it.
        
        # look at the next flower heap tip
        # if arrival time overlaps with it's bloom time
        # increase person one's view count
        
        # remove the heap tip
        # but store it somewhere, 
        # an array, `inView`
        
        # check the next tip
        # and repeat
        
        # if the next tip doesn't overlap
        # do we remove?
        # nah, since we have items in view
        # it means, this one is in the future.
        
        # we're done with this person.
        # we add the flowers in view back to
        # the flower heap
        # then pop the next person and repeat
        
        # one more thing, i want to report the blooms
        # in the same order the people are listed in the array.
        # in essence, when i heapify
        # i'd bundle with indices
        # so i know the original positions
        
        heapq.heapify(flowers)
        
        peepsAndIndices = [(arvTime, idx) for idx, arvTime in enumerate(people)]
        heapq.heapify(
            peepsAndIndices
        )
        
        bloomsSeen = []
        in_view = []
        
        while peepsAndIndices:
            arvTime, idx = heapq.heappop(peepsAndIndices)
            
            viewCount = 0
            while flowers and flowers[0][0] <= arvTime:
                flowerItem = heapq.heappop(flowers)
                bloomStart, bloomEnd = flowerItem
                
                if arvTime <= bloomEnd:
                    viewCount += 1
                    in_view.append(flowerItem)
                    
            bloomsSeen.append(
                (viewCount, idx)
            )
            while in_view:
                heapq.heappush(
                    flowers,
                    in_view.pop()
                )
                
        bloomsSeen.sort(key=lambda x: x[1])
        bloomsSeen = [viewCount for viewCount, _ in bloomsSeen]
        return bloomsSeen
    
arr = [
    [
        [[1,6],[3,7],[9,12],[4,13]],
        [2,3,7,11],
    ]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.fullBloomFlowers(foo, bar)
print(res)