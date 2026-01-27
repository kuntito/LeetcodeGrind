# https://leetcode.com/problems/minimum-path-sum/description/

from typing import List

# i'm given a grid, i want to move from top left to bottom right

# okay, what else? each cell of the grid has a value, an integer.

# every path, `topLeft` to `bottomRight` has a cost.
# the sum of the cells along that path.

# my job is to find the path with the lowest sum

# how would this work? my first thought is Dijkstra but it's not intuitive
# how i would track the sum of each path.

# why is Dijkstra unintuitive? because it's tracks the next smallest cell.

# well, what it tracks is entirely up to it's author. i mean, they named it
# but really, it's just a fancy way of using a minHeap.

# if you start at topLeft, you'd have two places you can go.
# down and right. if you append these to a minHeap, 
# append their (cell value and cell position)

# you immediately know which cell is cheaper to go to next.
# so you explore that cell.

# so what if it turns out the chosen cell has larger cell values ahead.
# well that's the beauty of the minHeap.

# for every cell, you explore, you append their down and right cells to the minHeap
# (cell value and cell position)

# so when picking the next cell from a minHeap, you always pick the one with the smallest
# cell value next.

# say you started at value `0`
# and can go to `3` or go to `5`

# naturally, you'd pick `3` first, since it's smaller.
# you append it's down and right neighbours to the minHeap.

# if it then turns out hat these neighbours are too large, i.e. `> 5`.
# because, we've added to the minHeap, they wouldn't be at the top.

# the minHeap would tell us, we should go to `3` next and that's the beauty of it.

# Dijkstra's is simply a wrapper round a minHeap.

# so how can you apply it to this question. well using the algorithm, we can definitely
# find the shortest path to `bottomRight`

# we just need the sum of along the shortest path. one way is to have every minHeap
# entry know it's own path sum.

# when you start at origin, the path is the value at origin.
# when you check

# originRight and originDown, the paths at those points

# are `origin + originRight` and `origin + originLeft` respectively.
# doing this allows us to know the path sum at each minHeap item.

# so, when we reach the end. we have our value.
# case closed.

import heapq

# so what do i need? a minHeap, 
# what does each entry look like
# (cellValue, cellPosition, pathSum)

# and the first entry would be (originCellValue, origin, originCellValue)
# do we want to track seen cell positions..

# i think we might, since we can end up at the same cell position via different paths
# i.e. starting from origin, rightDown and leftRight end up at the same point.

# yes, but with Dijkstra, whichever path we take first must have been the shortest path
# so it's safe to ignore that position again.

# yeah, at that position, whether, we did rightDown or leftRight, we end up doing the same thing
# in both instances..

# so i'd need to track seen positions, too
# right three variables so far..

# minHeap
# minHeapEntry
# a set

# okay, and what's the iteration look like, while minHeap is not empty?
# well, we could use while True, it wouldn't matter since, we're guaranteed to hit
# `bottomRight` at some point.

# TODO, pparently, i should be tracking `pathSum + neiValue` in the minHeap, not just `neiValue`
# it works, but i'm not sure why, essentially, you want to pick the next smallest path sum
# not the next smallest cell value

# but when would they be different?
# the failing test case is long, wonder if i can simplify it.
# [[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]

# without exploring the test case, i think i have the intuition from another question, `networkDelay`
# what you should store in the heap is the pathSum it takes to reach the current node.. not the value
# of the node itself..

# you can end up at the same node with different lengths..
# say:
# path1 => 6 => 4 => (2)
# path2 => 3 => 2 => (3)

# say both (2) and (3) can help us get to destination with the same sum onwards..
# with the way the algo is currently written, we'd prefer to explore (2)
# since the value is smaller, but we don't just care about the immediate next smaller value
# we care about it's history..

# getting to `2` requires 6 + 4 + 2 = 12
# getting to `3`, requires 3 + 2 + 3 = 8

# got it.. let me rewrite..

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        origin = (0, 0)
        seen = set()
        
        firstVal = grid[0][0]
        firstEntry = (firstVal, origin, firstVal)
        minHeap = [firstEntry]
        
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        bottomRight = (self.rows - 1, self.cols - 1)
        while True:
            curVal, curPos, pathSum = heapq.heappop(minHeap)
            
            if curPos in seen:
                continue
            
            seen.add(curPos)
            
            if curPos == bottomRight:
                return pathSum
            
            self.addDownRightNeighboursToHeap(curPos, pathSum, minHeap, seen)
            
            
    def addDownRightNeighboursToHeap(self, curPos, pathSum, minHeap, seen):
        r, c = curPos
        
        downCell = (r + 1, c)
        rightCell = (r, c + 1)
        
        neighbours = [downCell, rightCell]
        
        for nei in neighbours:
            if nei in seen: continue
            
            nR, nC = nei
            if nR < 0 or nR == self.rows or nC < 0 or nC == self.cols: continue
            
            neiValue = self.grid[nR][nC]
            heapq.heappush(
                minHeap,
                (
                    neiValue,
                    nei,
                    pathSum + neiValue                
                )
            )