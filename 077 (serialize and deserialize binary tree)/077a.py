# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'

from collections import deque

class Codec:
    # the idea is to obtain the preOrder traversal and inorderTraversal of the tree
    # represent these traversals as comma separated values
    # delimit both traversals with a &
    # i.e. F,O,O&B,A,R
    def __init__(self):
        self.delimiter = '&'
    
    # the use both traversals to deserialize into a binary tree
    def serialize(self, root) -> str:
        
        pass
    
        preOrder = []
        pre_csv = self.explore_preorder(root, preOrder)
        
        inOrder = []
        in_csv = self.explore_inorder(root, inOrder)


        get_csv = lambda arr: ",".join([str(dig) for dig in arr])
        pre_csv = get_csv(preOrder)
        in_csv = get_csv(inOrder)
        return f'{pre_csv}{self.delimiter}{in_csv}'

    def explore_preorder(self, root, arr):
        if not root:
            return
        
        arr.append(root.val)
        self.explore_preorder(root.left, arr)
        self.explore_preorder(root.right, arr)
        
        
    def explore_inorder(self, root, arr):
        if not root:
            return
        
        self.explore_inorder(root.left, arr)
        arr.append(root.val)
        self.explore_inorder(root.right, arr)
        

    def deserialize(self, data) -> TreeNode:
        pre_csv, in_csv = data.split(self.delimiter)
        
        comma = ','
        get_arr = lambda arr: [int(ch) for ch in arr.split(comma)]
        
        preorder = get_arr(pre_csv)
        inorder = get_arr(in_csv)
        in_map = {n: idx for idx, n in enumerate(inorder)}
        
        # print(in_map)
            
            
        return self.buildTree(preorder, inorder, in_map)
    
    # TODO the `in_map` solution only works if the node values are unique
    # how would you handle similar node values
    def buildTree(self, preorder, inorder, in_map):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        root_inorder_idx = in_map[root.val]
        end_range = root_inorder_idx + 1
        
        # left branch
        leftBranch = self.buildTree(
            preorder[1:end_range],
            inorder[:root_inorder_idx],
            in_map,
        )
        
        rightBranch = self.buildTree(
            preorder[end_range:],
            inorder[end_range:],
            in_map,
        )
        
        root.left = leftBranch
        root.right = rightBranch
        
        return root
        
        
        

three = TreeNode(3)
nine = TreeNode(9)
twenty = TreeNode(20)
fifteen = TreeNode(15)
seven = TreeNode(7)

twenty.left = fifteen
twenty.right = seven
three.left = nine
three.right = twenty


sol = Codec()
res = sol.serialize(three)
sol.deserialize(res)
# print(res)
