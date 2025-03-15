# https://leetcode.com/problems/reorganize-string/


import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        pass
    
        # maxHeap to store (ch, freq)
        
        # to form the string, create an array, `arr`
        # then while maxHeap is not empty
        # remove the most frequent char, `maxHeap[0]`
        # if it's different from `arr[-1]`, append
        # and update it's frequency
        # if the char is the same as `arr[-1]`
        # remove another element from the maxHeap, 
        # if it's also the same, it means there are no more unique chars
        # return ""
        # else update the frequency of the second removal and add both back to `maxHeap`
        
        # if frequency ever becomes zero, fashi
        counter = {}
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1
            
            
        maxHeap = [(-freq, ch) for ch, freq in counter.items()]
        heapq.heapify(maxHeap)
        
        arr = []
        while maxHeap:
            pass
            top = heapq.heappop(maxHeap)
            topFreq, topCh = top
            
            if arr:
                # if the chars are equal, you need another top
                if arr[-1] == topCh:
                    # if there's a top, get it else return ""
                    if maxHeap:
                        anotherTop = heapq.heappop(maxHeap)
                        atFreq, atCh = anotherTop
                        arr.append(atCh)
                        atFreq += 1
                        
                        if atFreq < 0:
                            heapq.heappush(maxHeap, (atFreq, atCh))
                    else:
                        return ""
                else:
                    arr.append(topCh)
                    topFreq += 1                
            else:
                arr.append(topCh)
                topFreq += 1
                
            if topFreq < 0:
                heapq.heappush(maxHeap, (topFreq, topCh))
                
            
        return "".join(arr)
        
        
arr = [
    "aab",
    "aaab",
]
foo = arr[-1]
sol = Solution()
res = sol.reorganizeString(foo)
print(res)
