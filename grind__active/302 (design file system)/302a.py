# https://leetcode.com/problems/design-file-system/description/

# this is a design question, what are we designing? a filesystem
# what are the requirements?

# can i take a moment to understand the question
# we want to create paths and paths in the file system are delimited by forward slashes

# an empty string or a single forward slash is not classed as a valid path
# eventhough all valid paths start with a forward slash

# we are to implement two functions, createPath and get
# createPath takes two arguments, a string `path` and a integer `value`
# it returns a boolean

# the function should create a new path and associate the integer value to it if possible. what does if possible mean? if the path already exists, return false
# if the path parent doesn't exist, return false

# the get function takes one argument, a string path and returns an integer.
# the function should return the integer value associated with a path or return -1
# if said path does not exist

# first, we need to figure out a way to store these paths
# each path is /XXX where XXX is tha path name
# we can divide a path into it's tokens. why though?

# whatever our storage is should allow us check for a path and it's value
# it's looking like a hashmap would be useful

# if we validate the paths, then add it to a hashmap
# assigning the value to the path
# that way we can modify the path

# once the path is created, we can't overwrite it
# this works however, when adding a new path, how do you know if the parent exists?

# i'm considering a tree structure
# for every path, we'd create a chain of nodes, every node has one parent
# but one parent can have multiple nodes

# and every node is associated with a value
# we might not need the hashmap after all, the plan would be to split a path into it's tokens
# and create nodes where necessary

# we can use a hashmap to store the root nodes of each file path
# i.e. /leet/code
# would have {"leet" -> Node("leet")}

# this way, creating a new path would mean we check for all the parent nodes and keep traversing till we hit the last node, at which point we simply create the leaf node and assign it a value

# so we need a node class
# it should have
# value: int
# path: str
# children: Node[]


class Node:
    def __init__(self, path: str, value: int, children) -> None:
        self.path = path
        self.value = value
        self.children = {}


class FileSystem:
    def __init__(self):
        pass
        # we would need a root node to hold all the root parents
        self.root(path="root", value=None)

        # this is the root from which all other paths stem from

    def createPath(self, path: str, value: int) -> bool:
        pass
        # once we have a path, we'd split it into tokens
        # a token is the string after the forward slash

        # but we also need to know if a string is valid
        # an empty string "" and "/" are not
        # we can do a simple check for this
        fwdSlash = "/"

        if path == "" or path == fwdSlash:
            return False

        # now, we have our tokens
        # we want to traverse from the first to last token and place it appropriately in `self.root`
        tokens = path.split(fwdSlash)

        # we want to place the token at index `0`
        # in root.children if it doesn't exist
        # if it does, we simply grab it and the next token i.e. index=1

        # we also want to ensure that the current index is not the last index
        # we also want to ensure that every parent of the leaf path exists
        # but what would that mean though

        # a -> b -> c
        self.placeTokens(0, tokens, value, self.root.children)

        # i think the idea here is that we only want to add the last path
        # in /a/b/c

        # when we call create path, we only want to create /c
        # so if /a or /b do not exist, return False

        # so technically the current token should always exist in root.children
        # else return False
        # the only time it's acceptable to not exist
        # the only time it's permissible to not exist
        # however, when idx == len(tokens) - 1
        # then we should create the new node and return False

    def placeTokens(self, idx, tokens, value, children):
        if idx == len(tokens) - 1:
            node = Node(
                path=tokens[idx],
                value=value,
            )
            return
        

    def get(self, path: str) -> int:
        pass
