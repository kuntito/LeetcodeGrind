class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'''({self.val},left={self.left},right={self.right})'''



class Solution:
    def find_min(self, node: TreeNode) -> int:
        temp = node
        while temp.left:
            temp = temp.left
        return temp.val

    def explore_delete(self, node: TreeNode, val: int) -> TreeNode:
        if not node: return None

        if val > node.val:
            node.right = self.explore_delete(node.right, val)
        elif val < node.val:
            node.left = self.explore_delete(node.left, val)
        else:
            if node.left and node.right:
                smallest_right_val = self.find_min(node.right)
                node.right = self.explore_delete(node.right, smallest_right_val)
                node.val = smallest_right_val
            else:
                res = node.left if node.left is not None else node.right
                node.left = None
                node.right = None
                return res
        return node

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        return self.explore_delete(root, key)

five = TreeNode(5)
three = TreeNode(3)
six = TreeNode(6)
two = TreeNode(2)
four = TreeNode(4)
seven = TreeNode(7)

three.right = four
three.left = two
six.right = seven
five.right = six
five.left = three

foo = Solution()
key = 3
node = five
res = foo.deleteNode(node, key)

print(res)