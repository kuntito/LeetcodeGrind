class KthLargest:
    def __init__(self, k: int, nums: list):
        self.arr = [None]
        self.k = k

        for n in nums:
            self.add(n)

    
    def add(self, val: int) -> int:
        if len(self.arr) == self.k + 1:
            if self.arr[1] >= val:
                return self.arr[1]
            self.arr[1] = val
            self.bubble_down()
        else:
            self.arr.append(val)
            self.bubble_up()

        return self.arr[1]


    def bubble_up(self):
        child = len(self.arr) - 1
        parent = child // 2

        while child > 1 and self.arr[parent] > self.arr[child]:
            self.arr[parent], self.arr[child] = self.arr[child], self.arr[parent]
            child = parent
            parent = child // 2


    def bubble_down(self):
        node_idx = 1
        node = self.arr[node_idx]

        left_ch = node_idx * 2
        right_ch = left_ch + 1

        while right_ch < len(self.arr) or left_ch < len(self.arr):
            node = self.arr[node_idx]
            left_ch = node_idx * 2
            right_ch = left_ch + 1
            
            if right_ch < len(self.arr) and\
                self.arr[right_ch] < self.arr[left_ch] and\
                self.arr[right_ch] < node:
                    self.arr[node_idx], self.arr[right_ch] = self.arr[right_ch], self.arr[node_idx]
                    node_idx = right_ch
            elif left_ch < len(self.arr) and self.arr[left_ch] < node:
                self.arr[node_idx], self.arr[left_ch] = self.arr[left_ch], self.arr[node_idx]
                node_idx = left_ch
            else:
                break





k = 2
nums = [0]
sol = KthLargest(k=k, nums=nums)

for n in [-1, 1, -2, -4, 3]:
    res = sol.add(n)
    print(res)


# k = 3
# nums = [4, 5, 8, 2]
# sol = KthLargest(k=k, nums=nums)

# for n in [3, 5, 10, 9, 4]:
#     res = sol.add(n)
#     print(res)


# k = 1
# nums = [1, 2, 2, 2, 2, 3]
# sol = KthLargest(k=k, nums=nums)

# for n in [4, 2, 5]:
#     res = sol.add(n)
#     print(res)