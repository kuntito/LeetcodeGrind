class KthLargest:
    def __init__(self, k: int, nums: list):
        self.lower_limit = -10**4
        self.upper_limit = 10 **4

        self.dict = {}
        self.max_val = self.lower_limit
        self.kth_elem = None
        self.k = k

        for n in nums:
            self.add_internal(n)

    def add(self, val: int) -> int:
        self.add_internal(val)
        self.update_kth_elem(val)
        return self.kth_elem
    

    def add_internal(self, val: int):
        if val not in self.dict:
            self.dict[val] = 0
        self.dict[val] += 1

        self.max_val = max(self.max_val, val)
        

    def update_kth_elem(self, val: int):
        if self.kth_elem is None:
            self.initialize_kth_elem()
            return
        
        if self.kth_elem > val:
            return
        
        self.dict[self.kth_elem] -= 1
        for n in range(self.kth_elem, self.upper_limit+1):
            if n in self.dict and self.dict[n] > 0:
                self.kth_elem = n
                break

        
    def initialize_kth_elem(self):
        count = 0
        for n in range(self.max_val, self.lower_limit-1, -1):
            if n in self.dict:
                count += self.dict[n]

            if count >= self.k:
                self.kth_elem = n
                self.dict[n] -= (count - self.k)
                return
            
k = 3
nums = [1, 2, 3, 3]
sol = KthLargest(k=k, nums=nums)

for n in [3, 5, 6, 7, 8]:
    res = sol.add(n)
    print(res)