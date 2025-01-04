from collections import deque

class Solution:
    def encode(self, strs: list[str]) -> str:
        self.queue = deque()
        for w in strs:
            self.queue.append(len(w))
        return ''.join(strs)

    def decode(self, s: str) -> list[str]:
        res = []

        index = 0
        while self.queue:
            output = ''
            count = self.queue.popleft()
            for _ in range(count):
                output += s[index]
                index += 1
            res.append(output)

        return res