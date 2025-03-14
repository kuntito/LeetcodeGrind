class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'''(
        {self.val},
        left={self.left},
        right={self.right}
    )'''



class Solution:
    def remove_min(self, root: TreeNode, node: TreeNode) -> TreeNode:
        parent = None
        temp = node
        while temp.left:
            parent = temp
            temp = temp.left
        
        # severing child
        if parent:
            parent.left = temp.right
        else:
            root.right = temp.right

        return temp


    def explore_delete(self, node: TreeNode, val: int) -> TreeNode:
        if not node: return None

        if val > node.val:
            node.right = self.explore_delete(node.right, val)
        elif val < node.val:
            node.left = self.explore_delete(node.left, val)
        else:
            if node.left and node.right:
                min_node = self.remove_min(node, node.right)
                min_node.left = node.left
                min_node.right = node.right
                return min_node
            else:
                return node.left if node.left else node.right
        
        return node



    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        return self.explore_delete(root, key)
    




two = TreeNode(2)
zero = TreeNode(0)
thirty_four = TreeNode(34)
eleven = TreeNode(11)
twenty_five = TreeNode(25)
thirty_one = TreeNode(31)
twenty_nine = TreeNode(29)
thirty_two = TreeNode(32)


two.left = zero
two.right = thirty_four
thirty_four.left = twenty_five
twenty_five.left = eleven
twenty_five.right = thirty_one
thirty_one.left = twenty_nine
thirty_one.right = thirty_two

key = 33
foo = Solution()
res = foo.deleteNode(two, key)

print(res.right.left.right)