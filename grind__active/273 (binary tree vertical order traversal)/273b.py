# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/

# Definition for a binary tree node.
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: TreeNode) -> list[list[int]]:
        pass
    
        # how do you determine the vertical order in a binary tree
        # we explore using a breadth first traversal
        # the idea is to use an integer to determine the current column index, `indicator`
        
        # consider
        #  3
        # 9 20
        
        # we explore 3 with `indicator == 0`
        # if we go left, we decrement the indicator by `1`
        # if we go right, we increment the indicator by `1`
        
        # then use a default dict
        # to track the elements at each indicator
        
        # the default dict would have kv pairs
        # indicator => [nodes with said indicator]
        
        # once, we have this structure, we can parse through the keys
        # of the default dict in order
        
        # each list represents each column of the binary tree
        
        # first, we need a queue
        queue = deque()
        
        # we add root and the indicator = 0
        # we should only do this if `node` is a valid node
        if root:
            queue.append((
                root,
                0
            ))
        
        # now, we need our default dict
        colsDict = defaultdict(list)
        
        while queue:
            dim = len(queue)
            
            # for each element in queue
            # we obtain the node and the indicator
            # and we add the left child to the queue with indicator - 1
            # and the right child with indicator + 1
            # then add the current node value to `colsDict`
            for _ in range(dim):
                node, indicator = queue.popleft()
                
                colsDict[indicator].append(node.val)
                
                leftChild = node.left
                if leftChild:
                    queue.append((
                        leftChild,
                        indicator - 1
                    ))
                
                rightChild = node.right
                if rightChild:
                    queue.append((
                        rightChild,
                        indicator + 1
                    ))
                    
        sortedCols = sorted(colsDict.keys())
        res = [colsDict[ci] for ci in sortedCols]
        
        return res
                    

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
print(res)