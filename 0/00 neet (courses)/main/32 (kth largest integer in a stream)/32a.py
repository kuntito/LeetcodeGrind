# https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:
    def __init__(self, k: int, nums: list):
        self.arr = [0]
        self.k = k
        self.dict = {}
        self.max_val = None
        self.kth_elem = None
        self.lower_limit = -10 ** 4
        self.upper_limit = 10 ** 4

        for n in nums:
            self.add_internal(n)
            self.update_max(n)


    def add(self, val: int) -> int:
        if self.max_val is None or self.kth_elem is None:
            self.update_max(val)
        self.add_internal(val)
        self.update_kth_element(val)
        return self.kth_elem


    def add_internal(self, val: int):
        if val not in self.dict:
            self.dict[val] = 0
        self.dict[val] += 1

        self.arr.append(val)
        self.bubble_up()


    def bubble_up(self):
        child = len(self.arr) - 1
        parent = child // 2

        while child > 1 and self.arr[parent] < self.arr[child]:
            self.arr[parent], self.arr[child] = self.arr[child], self.arr[parent]
            child = parent
            parent = child // 2


    def update_max(self, val: int):
        if self.max_val is None:
            self.max_val = val
            return
        
        self.max_val = max(self.max_val, val)


    def update_kth_element(self, val):
        if self.kth_elem is None:
            self.initialize_kth_element()
            return

        if self.kth_elem > val:
            return
        
        self.dict[self.kth_elem] -= 1
        for n in range(self.kth_elem, self.upper_limit + 1):
            if n in self.dict and self.dict[n] > 0:
                self.kth_elem = n
                return


    def initialize_kth_element(self):
        count = 0
        for n in range(self.max_val, self.lower_limit-1, -1):
            if n in self.dict:
                count += self.dict[n]

            if count >= self.k:
                self.kth_elem = n
                self.dict[self.kth_elem] -= (count - self.k)
                return


# k = 3
# nums = [1, 2, 3, 3]
# sol = KthLargest(k=k, nums=nums)

# for n in [3, 5, 6, 7, 8]:
#     res = sol.add(n)
#     print(res)

# k = 3
# nums = [1, 1]
# sol = KthLargest(k=k, nums=nums)

# for n in [1, 1, 3, 3, 3, 4, 4, 4]:
#     res = sol.add(n)
#     print(res)


# k = 1
# nums = []
# sol = KthLargest(k=k, nums=nums)

# for n in [-3, -2, -4, 0, 4]:
#     res = sol.add(n)
#     print(res)


# k = 3
# nums = [4, 5, 8, 2]
# sol = KthLargest(k=k, nums=nums)

# for n in [3, 5, 10, 9, 4]:
#     res = sol.add(n)
#     print(res)


# k = 3
# nums = [1, 1]
# sol = KthLargest(k=k, nums=nums)

# for n in [1, 1, 3, 3, 3, 4, 4, 4]:
#     res = sol.add(n)
#     print(n, '=>', res)


# k = 7
# nums = [-10,1,3,1,4,10,3,9,4,5,1]
# sol = KthLargest(k=k, nums=nums)

# for n in [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]:
#     res = sol.add(n)
#     print(res)


k = 1
nums = [1, 2, 2, 2, 2, 3]
sol = KthLargest(k=k, nums=nums)

for n in [4, 2, 5]:
    res = sol.add(n)
    print(res)