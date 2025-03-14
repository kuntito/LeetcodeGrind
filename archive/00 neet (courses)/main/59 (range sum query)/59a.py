# https://leetcode.com/problems/range-sum-query-mutable/description/


class SegmentNode:
    def __init__(self, l, r) -> None:
        self.left_ch: SegmentNode = None
        self.right_ch: SegmentNode = None
        self.somme = 0
        self.l = l
        self.r = r

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'{self.somme}, [{self.left_ch}, {self.right_ch}]'

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

        l, r = 0, len(nums) - 1
        self.root = self.add_node(l, r)



    def add_node(self, l, r):
        node = SegmentNode(
            l=l,
            r=r,
        )
        if l == r:
            node.sum = self.nums[l]
            return node
        
        mid = (r + l)//2

        node.left_ch = self.add_node(l, mid)
        node.right_ch = self.add_node(mid+1, r)
        node.sum = node.left_ch.sum + node.right_ch.sum

        return node
    

    def update(self, index: int, val: int) -> None:
        self.explore_update(self.root, index, val)
        # print(self.nums, sum(self.nums))

    def explore_update(self, node, target_idx, val):
        l, r = node.l, node.r
        if l == r:
            self.nums[target_idx] = val
            node.sum = val
            return

        mid = (node.r + node.l)//2
        if target_idx > mid:
            self.explore_update(node.right_ch, target_idx, val)
        else:
            self.explore_update(node.left_ch, target_idx, val)

        node.sum = node.left_ch.sum + node.right_ch.sum
        

    def sumRange(self, left: int, right: int) -> int:
        temp = self.root
        res =  self.explore_sum(left, right, temp)
        # print(res)
        return res
    
    def explore_sum(self, l, r, node: SegmentNode):
        if node.l == l and node.r == r:
            return node.sum

        mid = (node.r + node.l)//2
        if l > mid:
            return self.explore_sum(l, r, node.right_ch)
        elif r <= mid:
            return self.explore_sum(l, r, node.left_ch)
        else:
            return self.explore_sum(l, mid, node.left_ch) +\
                self.explore_sum(mid + 1, r, node.right_ch)



arr = [
    [0, 9, 5, 7, 3],
    [1, 3, 5],
    [7,2,7,2,0]
]

foo = arr[-1]
# print("og")
# print(foo)
sol = NumArray(foo)
sol.update(4,6)
sol.sumRange(0, 4)


sol.update(0,2)
sol.sumRange(0, 4)


sol.update(0,9)
sol.sumRange(0, 4)

# sol.sumRange(4,4)
sol.update(3,8)
sol.sumRange(0, 4)

# sol.sumRange(0,4)
# (4,1)
# (0,3)
# (0,4)
# (0,4)

