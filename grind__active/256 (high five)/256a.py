# https://leetcode.com/problems/high-five/description/

# TODO re-solve with custom sort
# sort by student id in ascending order then scores in descending order
# then pick first five for each unique id
import heapq
class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        pass
        # use a hashmap
        # student id => minHeap
        
        # the minHeap should never exceed length of 5
        # explore each id, score pair
        # for each id, obtain it's minHeap
        
        # add the new score if the minHeap size < 5
        # if the minHeap size == 5 and the new score > minHeap[0]
        # pop from the min heap and add the new score
        
        maxTrack = 5
        scoreMap = {}
        for stud_id, currScore in items:
            if stud_id not in scoreMap:
                scoreMap[stud_id] = []
                
            minHeap = scoreMap[stud_id]
            trackedScores = len(minHeap)
            
            if trackedScores < maxTrack or currScore > minHeap[0]:
                if trackedScores == maxTrack:
                    heapq.heappop(minHeap)
                    
                heapq.heappush(minHeap, currScore)
                
        res = []
        for stud_id in scoreMap:
            scores = scoreMap[stud_id]
            # print(stud_id, '=>', scores)
            total = sum(scores)
            avg = total // len(scores)
            
            res.append([stud_id, avg])
               
        res.sort()
        return res
     
arr = [
    [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]],
]
foo = arr[-1]
sol = Solution()
res = sol.highFive(foo)
print(res)
            