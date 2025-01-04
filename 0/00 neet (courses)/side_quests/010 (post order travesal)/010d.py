class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'


class Solution:
    def postorderTraversal(self, root: Node) -> list:
        arr, seen, post_order = [root], [False], []

        while arr:
            curr, visited = arr.pop(), seen.pop()
            if curr:
                if visited:
                    post_order.append(curr.val)
                else:
                    self.append_values(arr, seen, curr, True)
                    self.append_values(arr, seen, curr.right, False)
                    self.append_values(arr, seen, curr.left, False)
        return post_order
    
    
    def append_values(self, iter_uno, iter_dos, uno, dos):
        iter_uno.append(uno)
        iter_dos.append(dos)


one = Node(1)
two = Node(2)
three = Node(3)

two.left = three
one.right = two

sol = Solution()
res = sol.postorderTraversal(one)

print(res)
