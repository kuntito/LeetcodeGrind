# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'

from collections import deque

# TODO write out the pseudocode
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/ shows a binary tree can be constructed from it's preorder and inorder traversal
class Codec:

    def serialize(self, root):
        inorder = []
        preorder = []
        self.exploreInOrder(root, inorder)
        self.explorePreOrder(root, preorder)

        res = []
        for preNode, inNode in zip(inorder, preorder):
            res.append(
                f"{preNode}-{inNode}"
            )

        return ",".join(res)


    def exploreInOrder(self, root, arr):
        if not root:
            return
        
        self.exploreInOrder(root.left, arr)
        arr.append(root.val)
        self.exploreInOrder(root.right, arr)

    def explorePreOrder(self, root, arr):
        if not root: return

        arr.append(root.val)
        self.explorePreOrder(root.left, arr)
        self.explorePreOrder(root.right, arr)
        

    def deserialize(self, data):
        preorder = []
        inorder = []

        for item in data.split(","):
            preNode, inNode = item.split("-")
            preorder.append(int(preNode))
            inorder.append(int(inNode))

        return self.buildTree(preorder, inorder)
    
    # TODO, build binary tree from preorder and inorder lists
    def buildTree(self, preorder, inorder):
        if not preorder: # TODO this might be a string
            return None

        in_map = { n: idx for idx, n in enumerate(inorder) }

        root = Node(preorder[0])
        
        parent = root
        dim = len(preorder)
        for idx in range(1, dim):
            pass
            n = preorder[idx]
            parent_idx = in_map[parent.val]
            if idx < parent_idx:
                parent.left = self.buildTree(
                    preorder[idx:],
                    inorder[
                        in_map[n] + 1 : parent_idx
                    ]
                )
                
        return root
            
            
            


three = Node(3)
nine = Node(9)
twenty = Node(20)
fifteen = Node(15)
seven = Node(7)

twenty.left = fifteen
twenty.right = seven
three.left = nine
three.right = twenty


sol = Codec()
# sol.serialize(three)
# TODO test the recursive tree building
sol.buildTree(
    [3,9,20,15,7],
    [9,3,15,20,7]
)
