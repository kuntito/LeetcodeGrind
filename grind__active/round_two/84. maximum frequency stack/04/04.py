import heapq

class FreqStack:
    def __init__(self):
        self.maxHeap = []
        self.numFreqMap = {}
        
        # and how do i track recency?
        # i can declare a global integer, `recency`
        # and increment it whenever i add a number
        # this way, the recency reflects the recency of each number.
        self.recency = 0

    def push(self, val: int) -> None:
        # what does pushing look like?
        # you update frequency
        self.numFreqMap[val] = self.numFreqMap.get(val, 0) + 1
        
        # you update recency
        self.recency += 1
        
        # you add a heap item
        freq = self.numFreqMap[val]
        
        # python has no innate maxHeap, so we negate the sorting values
        # to simulate a max heap
        # freq becomes (-1 * freq)
        # recency becomes (-1 * freq)
        heapItem = (
            -1 * freq, 
            -1 * self.recency, 
            val
        )
        
        heapq.heappush(
            self.maxHeap,
            heapItem
        )

    def pop(self) -> int:
        # what does popping look like
        # take off the heap top.
        
        topItem = heapq.heappop(self.maxHeap)
        
        negFreq, negRecency, number = topItem
        
        # so what do i want to do?
        # i want to update frequency
        
        # then return the number at the top
        
        self.numFreqMap[number] -= 1
        
        # turns out i don't need `negFreq` and `negRecency`
        
        return number