class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # perform a bst on the tree
        # store all values in an array
        # use 'n' to denote the absence of a child node
        
        arr = []
        
        layer = [root]
        while layer:
            tmp = []
            for curr in layer:
                arr.append(curr)
                
                if curr == 'N': continue
                
                leftChild = curr.left if curr.left else 'N'
                rightChild = curr.right if curr.right else 'N'
                
                tmp.append(leftChild)
                tmp.append(rightChild)
                
            layer = tmp
            
        print(arr)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
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