
import heapq


heap = [(0, i) for i in range(5)]
heapq.heapify(heap)

while heap:
    print(heapq.heappop(heap))
