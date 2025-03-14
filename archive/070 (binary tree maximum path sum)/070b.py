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
    def maxPathSum(self, root: TreeNode) -> int:
        pass
        
        return self.explore(root, float("-infinity"))[1]
        
    # each node returns the max path from itself
    # i.e. max(node + left, node.right)
    
    # but it updates itself based on node + left + right
    # why not left iso or right iso
    # because the recursive branch of the iso's would have handled that
    # the only thing we need to handle is the sum of everything
    
    # what if the sum is left + node OR right + node
    # if the better sum is left + node, it means the right node is negative subtotal
    
    # if the better sum is right + node, it means the left node is negative subtotal
    
    # in both cases, it makes sense to do `left = max(left, 0)`
    def explore(self, root, bestSoFar):
        if not root:
            return 0, bestSoFar
        
        leftRes, foo = self.explore(root.left, bestSoFar)
        bestSoFar = max(foo, bestSoFar)
        
        rightRes, foo = self.explore(root.right, bestSoFar)
        bestSoFar = max(foo, bestSoFar)
        
        left = max(leftRes, 0)
        right = max(rightRes, 0)
        
        
        bestPath = max(root.val + left, root.val + right)
        bestSoFar = max(bestSoFar, root.val + left + right)
        return bestPath, bestSoFar
        
        
neg_ten = TreeNode(-10)
nine = TreeNode(9)
twenty = TreeNode(20)
fifteen = TreeNode(15)
seven = TreeNode(7)
        
        
neg_ten.left = nine
neg_ten.right = twenty
twenty.left = fifteen
twenty.right = seven


sol = Solution()
res = sol.maxPathSum(neg_ten)
print(res)