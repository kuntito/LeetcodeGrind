# https://leetcode.com/problems/word-ladder/description/


import heapq
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        begin_found, end_found = self.is_words_in_list(beginWord, endWord, wordList)

        if not begin_found:
            wordList.append(beginWord)

        if not end_found:
            return 0

        graph = self.create_graph(wordList)
        # print(graph)

        # can you reach `beginWord` from`endWord`
        return self.explore(beginWord, endWord, graph)

    # a graph where each word's neighbours are all the words it can reach with one transformation  
    def create_graph(self, wordList):
        patterns = self.create_patterns(wordList)
        graph = {}
        for word in wordList:
            graph[word] = []
            for pat in self.get_word_patterns(word):
                for nei in patterns[pat]:
                    if nei != word:
                        graph[word].append(nei)

        return graph


    def create_patterns(self, wordList):
        patterns = {}
        for word in wordList:
            for pat in self.get_word_patterns(word):
                self.add_to_patterns(pat, patterns, word)
        return patterns

    def get_word_patterns(self, word):
        res = []
        word = list(word)
        for idx, ch in enumerate(word):
            word[idx] = "*"
            res.append(
                "".join(word)
            )
            word[idx] = ch

        return res

    def add_to_patterns(self, pat, patterns, word):
        if pat not in patterns:
            patterns[pat] = set()

        patterns[pat].add(word)


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