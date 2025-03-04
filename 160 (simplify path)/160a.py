# https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        pass
        # remove all the ending slashes
        
        # the path must start with a single slash
        
        # separate the `path` into tokens
        # where each token starts with a forward slash
        # contains at least one character 
        # and ends right before another forward slash
        
        tokens = []
        tmp = []
        
        
        fwd_slash = '/'
        if path[0] != fwd_slash:
            tmp.append(fwd_slash)
        for idx, ch in enumerate(path):
            pass
            if len(tmp) >= 2 and ch == fwd_slash:
                tokens.append("".join(tmp))
                tmp = []
                
            if ch == fwd_slash and tmp and tmp[-1] == fwd_slash:
                continue
            
            tmp.append(ch)
            
        tokens.append("".join(tmp))
        
        if tokens[-1] == fwd_slash:
            tokens.pop()

        res = []
        
        for tk in tokens:
            if tk == '/..':
                if res:
                    res.pop()
            elif tk == '/.':
                continue
            else:
                res.append(tk)
                
        if not res:
            return fwd_slash
        
        return "".join(res)
        
arr = [
    "/.../a/../b/c/../d/./",
     "/../",
     "/home/user/Documents/../Pictures",
     "/home//foo/",
    "/home/",
]
foo = arr[-1]
sol = Solution()
res = sol.simplifyPath(foo)
print(res)
