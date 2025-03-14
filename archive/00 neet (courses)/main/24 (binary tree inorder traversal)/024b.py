class Solution:
    def inorderTraversal(self, root):
        res = []
        if root is None: return res

        stack = [root]
        seen = set()
        seen.add(root)
        while stack:
            cur_node = stack[-1]
            while cur_node.left and cur_node.left not in seen:
                stack.append(cur_node.left)
                seen.add(cur_node.left)
                cur_node = stack[-1]
            else:
                stack.pop()
                res.append(cur_node.val)
                if cur_node.right:
                    stack.append(cur_node.right)
                
        return res