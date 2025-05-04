# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/


# Definition for a binary tree node.
from typing import List, Optional

# TODO it returns the nodes in their respective columns
# but it doesn't address the same row, same column logic
# see:
# Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
# Output: [[4],[2,5],[1,10,9,6],[3],[11]]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f"({self.val})"


from collections import deque


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass
        # what determines the vertical order of a node
        # it's easy to visualize it but how do you write the code
        # the first column is the left most node

        # the first thing is to determine the total number of columns
        # declare an array, `cols` to store all the column info
        # from the root node, explore leftwards till you hit the leftmost leaf node

        # that node represents the first column
        # put that node in an array and add that array to columns
        # as the recursion moves up, add subsequent sub roots to the array
        # put them in an array and add to `cols`

        # that way `cols` contains the first node in every column
        # put `root` in an array, add to `cols`

        # for every node added to `cols`
        # put it in a `queue`
        # you need a mapping of every node to it's column index in `cols`

        # now for every node in the queue
        # we explore it's left and right child nodes

        # since we know the nodes column index
        # the left child would be in `column index - 1`
        # and the right child would be in `column index + 1`

        # if `columnIndex + 1` does not exist create it
        # for every new child node, append to the queue

        cols = []
        queue = deque()
        seen = set()

        self.exploreLeft(root, cols, queue, seen)

        while queue:
            node, colIdx = queue.popleft()
            
            
            leftChild, rightChild = node.left, node.right
            
            if leftChild and leftChild not in seen:
                cols[colIdx - 1].append(leftChild.val)
                queue.append(
                    (leftChild, colIdx - 1)
                )
                
            if rightChild and rightChild not in seen:
                # if the next column does not exist
                if colIdx + 1 == len(cols):
                    cols.append([])
                    
                cols[colIdx + 1].append(rightChild.val)
                queue.append(
                    (rightChild, colIdx + 1)
                )
                
        return cols


    def exploreLeft(self, root, cols, queue: deque, seen):
        if not root:
            return

        self.exploreLeft(root.left, cols, queue, seen)

        # create the column array that stores all the column values
        colArr = [root.val]

        # append that array to the global cols, which is the final result
        cols.append(colArr)

        # append the node to the queue so we can access it's children
        # we append the node and it's column index
        colIdx = len(cols) - 1
        queue.append((root, colIdx))
        seen.add(root)


three = TreeNode(3)
nine = TreeNode(9)
eight = TreeNode(8)
four = TreeNode(4)
zero = TreeNode(0)
one = TreeNode(1)
seven = TreeNode(7)

three.left = nine
three.right = eight

nine.left = four
nine.right = zero

eight.left = one
eight.right = seven

sol = Solution()
res = sol.verticalOrder(three)