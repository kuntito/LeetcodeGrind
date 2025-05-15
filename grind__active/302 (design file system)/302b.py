# https://leetcode.com/problems/design-file-system/description/

# we want to design a file system, we're using a class
# with two methods, `createPath` and `get`

# `createPath` takes two arguments a string `path` and an integer `value`
# every path has a value assigned to it

# and this value is the what the `get` method returns

# going back to `createPath`, the string `path`
# represents a path, a valid path starts with a forward slash "/" and some text
# a forward slash in isolation is not a valid path and an empty string "" is not a valid path

# our job, when `createPath` is called is to store the `path` and the value associated with it
# and return True if successful

# however, if the path already exists or it's parent path doesn't exist, we should return False

# my understanding of this is- let's consider the path
# /leetcode/rules

# what we really want to add is /rules
# the parent is assumed to exist
# we check if the parent exists, if not, we return False

# in some sense i could use a hashmap to store the parents
# so for every new path, i extract it's parent, if the parent is valid
# i add the new path and value to the hashmap
# but i should ensure the path doesn't already exist in the hashmap

# i should also ensure the path is valid from the jump
class FileSystem:
    def __init__(self):
        self.pathMap = {}
        self.pathMap[""] = 0

    def createPath(self, path: str, value: int) -> bool:
        fwdSlash = "/"
        if path == "" or path == fwdSlash:
            return False
        
        parent, _ = path.rsplit(fwdSlash, maxsplit=1)
        # if the parent is an empty string, it means
        # we're dealing with a root path i.e. /leet
        # so we should add the path directly provided it doesn't already exist
        # i'd address this by adding the empty string in the hashmap from the jump
        if (parent not in self.pathMap) or (path in self.pathMap):
            return False
        
        self.pathMap[path] = value
            
        return True

    def get(self, path: str) -> int:
        return self.pathMap.get(path, -1)

sol = FileSystem()
sol.createPath("/leet", 2)