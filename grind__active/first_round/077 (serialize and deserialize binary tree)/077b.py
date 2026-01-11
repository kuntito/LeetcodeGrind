# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# TODO https://neetcode.io/solutions/serialize-and-deserialize-binary-tree
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
    def __init__(self):
        self.delim = '&'
        self.dupSep = '@'

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        # perform a in order and pre order traversal on the tree
        # since duplicates can exist
        # use a hashmap to indicate each unique value
        # let's say there are two nodes with value `2`
        # for the first `2`, check the hashmap
        # if the value is absent, add it i.e. {2: 1}
        # but what you append to the preorder array is "2-1"
        # if you find another two, increment it's frequency in the hashmap
        # and add "2-2" to the array
        
        # but how would you know the inorder and preorder are labelling the right nodes
        
        # it makes more sense to modify the nodes
        # with the hashvalue concept
        # for each value, if it's the first of it's kind
        # change it to `val-freq`
        
        self.markDuplicates(root, {})

        
        # then perform a regular preorder and inorder traversal
        # when deserializing, take note TODO
        preOrder = self.explorePreOrder(root, [])
        inOrder = self.exploreInOrder(root, [])
        
        get_csv = lambda x: ",".join(val for val in x)
        # to serialize, convert each array to a csv values and concatenate with ampersand
        preCsv = get_csv(preOrder)
        inCsv = get_csv(inOrder)
        
        res = preCsv + self.delim + inCsv
        return res
    
        
    def explorePreOrder(self, root, arr):
        if not root:
            return
        
        arr.append(root.val)
        self.explorePreOrder(root.left, arr)
        self.explorePreOrder(root.right, arr)
        
        return arr
        
            
    def exploreInOrder(self, root, arr):
        if not root:
            return
        
        self.exploreInOrder(root.left, arr)
        arr.append(root.val)
        self.exploreInOrder(root.right, arr)
        
        return arr
        
    def printByLayer(self, root):
        temp = [root]
        
        while temp:
            another = []
            print([x for x in temp])
            while temp:
                curr = temp.pop()
                if curr.left:
                    another.append(curr.left)
                if curr.right:
                    another.append(curr.right)
                    
            temp = another
        
        
    def markDuplicates(self, root, dupMap):
        if not root:
            return
        
        val = root.val
        if val not in dupMap:
            dupMap[val] = -1
            
        dupMap[val] += 1
        freq = dupMap[val]
        
        root.val = f"{val}{self.dupSep}{freq}"
        
        self.markDuplicates(root.left, dupMap)
        self.markDuplicates(root.right, dupMap)
        


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        comma = ','
        # separate the preCsv and inCsv
        preCsv, inCsv = data.split(self.delim)
        # convert them to arrays
        preOrder = preCsv.split(comma)
        inOrder = inCsv.split(comma)
        
        # use the arrays to reconstruct the tree
        root = self.buildTree(preOrder, inOrder)
        
        # remove the duplicate markers
        self.unmarkDuplicates(root)
        # self.printByLayer(root)
        
        return root
    
    def unmarkDuplicates(self, root):
        if not root:
            return
        
        remove_sep_convert_to_num = lambda x: int(x.split(self.dupSep)[0])
        root.val = remove_sep_convert_to_num(root.val)
        
        self.unmarkDuplicates(root.left)
        self.unmarkDuplicates(root.right)
        
        
    def buildTree(self, preOrder, inOrder):
        if not preOrder:
            return
        
        # the first element in preOrder is the root node
        rootVal = preOrder[0]
        root = TreeNode(rootVal)
        
        
        # find the index of rootVal in `inMap`, `rootInMapIdx`
        rootInMapIdx = inOrder.index(rootVal)
        # every thing to the left of rootInMapIdx is the left child of root
        # everything to the right is the right child
        # perform recursive functions on each sub array to find the left and right children
        leftInOrder = inOrder[:rootInMapIdx]
    
        leftEndRange = len(leftInOrder) + 1
        leftPreOrder = preOrder[1:leftEndRange]
        
        root.left = self.buildTree(
            preOrder=leftPreOrder,
            inOrder=leftInOrder,
        )
        

        rightInOrder = inOrder[rootInMapIdx+1:]
        rightPreOrder = preOrder[leftEndRange: leftEndRange + len(rightInOrder)]
        
        root.right = self.buildTree(
            preOrder=rightPreOrder,
            inOrder=rightInOrder,
        )
        
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
