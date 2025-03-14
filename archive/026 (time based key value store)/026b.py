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
        res = ""

        lst = self.collection.get(key, [])
        s, e = 0, len(lst)

        while s < e:
            mid = (s + e)//2
            item = lst[mid][0]

            if timestamp > item:
                s += 1
            else:
                res = lst[mid][0]
        
        return res