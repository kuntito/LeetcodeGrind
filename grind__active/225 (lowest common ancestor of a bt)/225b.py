# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __str__(self):
        return f'({self.val})'
        
    def __repr__(self):
        return str(self)
        

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', targetNodes: 'list[TreeNode]') -> 'TreeNode':
        if len(targetNodes) == 1:
            return targetNodes[0]
        
        # you want to traverse the entire tree
        # and determine if each node has a target node in it's subtree
        # itself included
        
        # use a hashmap for this
        self.targetsMap = {}
        targetNodes = set(targetNodes)
        
        self.exploreTargets(root, targetNodes)
        
        # print(self.targetsMap)
        
        return self.exploreAncestor(root, targetNodes)
        
    def exploreAncestor(self, root, targetNodes):
        if not root:
            return
        
        if root in targetNodes:
            return root
        
        if root.left and root.right and self.targetsMap[root.left] and self.targetsMap[root.right]:
            return root
        
        if root.left and self.targetsMap[root.left]:
            return self.exploreAncestor(root.left, targetNodes)
            
        return self.exploreAncestor(root.right, targetNodes)
        
        
        
    def exploreTargets(self, root, targetNodes, hasTarget=False):
        if not root:
            return False

        if root in targetNodes:
            hasTarget = True
        
        if self.exploreTargets(root.left, targetNodes):
            hasTarget = True
        if self.exploreTargets(root.right, targetNodes):
            hasTarget = True
        
        self.targetsMap[root] = hasTarget
        return self.targetsMap[root]
                
        
three = TreeNode(3)
five = TreeNode(5)
one = TreeNode(1)
six = TreeNode(6)
two = TreeNode(2)
zero = TreeNode(0)
eight = TreeNode(8)
seven = TreeNode(7)
four = TreeNode(4)

three.left = five
three.right = one

five.left = six
five.right = two

one.left = zero
one.right = eight

two.left = seven
two.right = four

sol = Solution()
res = sol.lowestCommonAncestor(three, [seven, six, two, four])
# res = sol.lowestCommonAncestor(three, [four, seven])

print('res is', res)
