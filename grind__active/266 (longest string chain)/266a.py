# https://leetcode.com/problems/longest-string-chain/description/

from collections import defaultdict


class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        pass
        # for each word, we want to know every word with which it differs by one character and their relative order is maintained

        # then we want to know the longest chain
        # for one, the words in the chain would differ by one character
        # we can have buckets for words of a particular length

        # consider: ["a","b","ba","bca","bda","bdca"]
        # the `1` bucket is `a` and `b`
        # the `2` bucket is `ba`
        # the `3` bucket is `bca` and `bcd`

        # starting with the `1` bucket
        # we explore every word in the `2` bucket for a viable chain
        # if we find one, we continue the chain until we can no longer move forward
        # at which point move on to numbers in the `2` bucket
        # it's posisble the longest chain could start in the two bucket

        # might be easier, if we did this using dp
        # and iterate backwards, starting from the largest bucket
        # what's the longest chain we can form from here?

        # but it's not just about chain, you still need to connect the words
        # imagine you had a graph and wanted to find the longest set of edges
        # what would you do?

        # it would be a dfs from every node and track the length
        # so first, connect all words in a graph
        # run dfs, voila

        # it's slightly easier since for every word, you only need to check for connections with words in the next bucket or previous buckets

        # first, we create a hashmap of buckets
        buckets = defaultdict(list)
        for w in words:
            size = len(w)
            buckets[size].append(w)

        order = sorted(list(buckets.keys()))
        graph = self.getGraph(buckets, order)

        # for k, v in graph.items():
        #     print(k, '=>', v)

        maxDepth = 0
        # seen = set()

        # self.final = order[-1]
        for idx, bi in enumerate(order):
            for w in buckets[bi]:
                depth = self.exploreDepth(w, graph)
                maxDepth = max(depth, maxDepth)
                if depth == len(order) - idx:
                    return maxDepth

        return maxDepth

    def exploreDepth(self, word, graph):
        depth = 0
        for nei in graph[word]:
            depth = max(depth, self.exploreDepth(nei, graph))

        return depth + 1

    def getGraph(self, buckets, order):
        # to create the graph, we explore the buckets in order
        # for every word in a bucket, we check every word in the next bucket for a connection
        # if we find, we create a two connection between both words
        # when we've explored the bucket, we move on to the next

        # it's important, we explore the buckets in increasing order
        # since while a word can connect forward, it can also connect backwards
        # and since, we explore in order, we create the forward connection for the first word and the backward connection for the next word

        # the first bucket has no backward connections

        graph = defaultdict(list)

        for bi in order:
            for w in buckets[bi]:
                nextBucket = bi + 1
                if nextBucket not in buckets:
                    continue
                self.connectIfPossible(w, buckets[nextBucket], graph)

        return graph

    def connectIfPossible(self, leftWord, arr, graph):
        for w in arr:
            if self.ifOrderSame(leftWord, w):
                # graph[w].append(leftWord)
                graph[leftWord].append(w)

    def ifOrderSame(self, wordOne, wordTwo):
        # wordTwo is longer than wordOne
        # set two indices, `uno` and `dos`

        # move them both at the same time
        # at some point, i expect their values to be different
        # that would represent the omission
        # but the omission should not happen more than once

        count = 0
        for idx, ch in enumerate(wordOne):
            if ch != wordTwo[idx + count]:
                count += 1

            if count > 1:
                return False

        return True


arr = [
    ["a", "b", "ba", "bca", "bda", "bdca"],
    ["xbc","pcxbcf","xb","cxbc","pcxbc"],
    ["a","b","ab","bac"]
]
foo = arr[-1]
sol = Solution()
res = sol.longestStrChain(foo)
# res = sol.ifOrderSame("bca", "abca")
print(res)
