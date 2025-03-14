# https://leetcode.com/problems/word-ladder/description/

import heapq
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        begin_found, end_found = self.is_words_in_list(beginWord, endWord, wordList)

        if not begin_found:
            wordList.append(beginWord)

        if not end_found:
            return 0

        graph = {}
        for w in wordList:
            graph[w] = []

        # create a weighted graph where all edges are `1`
        dim =  len(wordList)
        for i in range(dim):
            wordOne = wordList[i]
            for j in range(i+1, dim):
                wordTwo = wordList[j]
                if self.is_differ_by_one(wordOne, wordTwo):
                    self.addToGraph(wordOne, wordTwo, graph)

        # can you reach `beginWord` from`endWord`
        return self.explore(beginWord, endWord, graph)


    def is_words_in_list(self, uno, dos, wordList):
        uno_found = False
        dos_found = False

        for w in wordList:
            if w == uno:
                uno_found = True
            if w == dos:
                dos_found = True

            if uno_found and dos_found:
                break


        return uno_found, dos_found
    

    def explore(self, currWord, targetWord, graph):
        minHeap = [(1, currWord)]
        seen = set()

        while minHeap:
            node = heapq.heappop(minHeap)
            dist, curr = node

            if curr == targetWord:
                return dist

            if curr in seen:
                continue
            seen.add(curr)

            for nei in graph[curr]:
                neiNode = (dist + 1, nei)
                heapq.heappush(minHeap, neiNode)

        return 0


    def addToGraph(self, one, two, graph):
        graph[one].append(two)
        graph[two].append(one)


    def is_differ_by_one(self, uno, dos):
        count = 0
        for chOne, chTwo in zip(uno, dos):
            if chOne != chTwo:
                count += 1

            if count > 1:
                return False
            
        return count == 1





arr = [
    ["hit", "hot", ["hot"]],
    ["hit", "cog", ["hot","dot","dog","lot","log"]],
    ["hit", "cog", ["hot","dot","tog","cog"]],
    ["hit", "cog", ["hot","dot","dog","lot","log","cog"]],
]
uno, dos, tres = arr[-1]
sol = Solution()#
res = sol.ladderLength(uno, dos, tres)
print(res)