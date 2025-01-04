# https://leetcode.com/problems/design-browser-history/description/

class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.prev =  None
        self.next = None

    def __str__(self) -> str:
        return f'[val={self.val}, next={self.next}]'

    def __repr__(self) -> str:
        return str(self)


class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        node = Node(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = node


    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


a = Node("vibes")

print(a.prev)