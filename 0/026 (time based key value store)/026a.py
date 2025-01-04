# https://leetcode.com/problems/time-based-key-value-store/submissions/1403272547/


class TimeMap:
    def __init__(self):
        self.collection = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.collection:
            self.collection[key] = []

        self.collection[key].append(
            (timestamp, value)
        )

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.collection:
            return ""
        

        lst = self.collection[key]
        is_found, idx = self.bin_search(timestamp, lst)
        if is_found:
            return lst[idx][1]
        
        for i in range(idx-1, -1, -1):
            return lst[i][1]
        
        return ""



    def bin_search(self, target, lst):
        start, end = 0, len(lst)

        while start < end:
            mid = (start + end)//2
            mid_elem = lst[mid][0]
            if mid_elem == target:
                return (True, mid)
            elif target > mid_elem:
                start = mid + 1
            else:
                end = mid

        return (False, start)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

sol = TimeMap()
sol.set("foo", "bar", 1)
print(sol.get("foo", 0))
