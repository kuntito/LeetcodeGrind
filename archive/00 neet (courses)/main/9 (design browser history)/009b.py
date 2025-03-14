# https://leetcode.com/problems/design-browser-history/description/


class BrowserHistory:
    def __init__(self, homepage: str):
        self.index = 0
        self.max_index = 0
        self.arr = [homepage]

    def visit(self, url: str) -> None:
        self.index += 1
        self.max_index = self.index

        if self.index < len(self.arr):
            self.arr[self.index] = url
        else:
            self.arr.append(url)

    def back(self, steps: int) -> str:
        self.index = max(self.index - steps, 0)
        return self.arr[self.index]


    def forward(self, steps: int) -> str:
        self.index = min(self.index + steps, self.max_index)
        return self.arr[self.index]



a = [1, 2]
a[2] = 3

print(a)