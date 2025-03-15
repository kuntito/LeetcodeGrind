# https://leetcode.com/problems/design-hashset/description/

# TODO https://www.youtube.com/watch?v=VymjPQUXjL8
# TODO can you expand box on-demand?
# TODO can you accomodate `1_000_000`
class MyHashSet:
    def __init__(self):
        self.max_count = 1_000_000
        # split into 100 boxes
        self.sub_count = 100
        self.box_size = self.max_count // self.sub_count

        self.arr_map = {}

        self.is_milli = False

    def add(self, key: int) -> None:
        if key == self.max_count:
            self.max_count = True
            return

        # what box is it in?
        box_idx, rem = divmod(key, self.sub_count)

        if box_idx not in self.arr_map:
            self.arr_map[box_idx] = []
        
        box = self.arr_map[box_idx]

        # where should key be placed in box?
        idx_in_box = rem
        
        self.validate_size(idx_in_box, box)

        box[idx_in_box] = True
        

    def validate_size(self, idx, box):
        if len(box) > idx:
            return
        # TODO
        # `x` is the amount of slots `box` would need to accomodate `idx`
        # but it should be capped at self.box_size
        x = 0
        box += [False for _ in range(x)]


    def remove(self, key: int) -> None:
        if key == self.max_count:
            self.is_milli = False
            return self.is_milli

    def contains(self, key: int) -> bool:
        if key == self.max_count:
            return self.is_milli