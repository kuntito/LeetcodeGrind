# https://leetcode.com/problems/house-robber-iii/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'
        
class Solution:
    def rob(self, root: TreeNode) -> int:
        pass

            
        # each node should return it's maxRob
        # for a leaf node, it's maxRob is itself
        
        # for a node with two children
        # it's maxRob is the max of itself and the sum of it's children
        
        # each node should return two things, it's maxRob and the maxRobChildren
        
        # fixing the condition above,
        # each node's maxRob is the max(itself + childrensChildren, children)
        return self.explore(root)[0]
        
    def explore(self, root):
        if not root:
            return [0, 0]
        
        if self.is_leaf(root):
            return [root.val, 0]
        
        maxLeft, maxLeftChild = self.explore(root.left)            
        maxRight, maxRightChild = self.explore(root.right)
        
        maxRobChildren = maxLeft + maxRight
        
        maxRobHere = max(
            root.val + maxLeftChild + maxRightChild,
            maxRobChildren
        )
        
        return maxRobHere, maxRobChildren
        
        
        
    def is_leaf(self, node):
        return node.left is None and node.right is None
    
    
three = TreeNode(3)
two = TreeNode(2)
three2 = TreeNode(3)
three3 = TreeNode(3)
one = TreeNode(1)

two.right = three3
three2.right = one
three.left = two
three.right = three2

sol = Solution()
res = sol.rob(three)
print(res)