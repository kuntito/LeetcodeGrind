# https://leetcode.com/problems/detect-squares/description/

# TODO https://neetcode.io/solutions/detect-squares
class DetectSquares:
    def __init__(self):
        pass
        # hashmap for storing points
        self.points = {}
        # keys are positions, (x, y)
        # values representing the frequency of each position

        # create hashmaps for `x_axes` and `y_axes`
        # the key for `x_axes` is the `x` value, the value is a set containing the positions
        self.x_axes = {}
        # the key for the `y_axes` is the `y` value, and the value is a set containing the positions
        self.y_axes = {}


    def add(self, point) -> None:
        point = tuple(point)
        self.points[point] = self.points.get(point, 0) + 1
        
        x, y = point
        if x not in self.x_axes:
            self.x_axes[x] = set()
        self.x_axes[x].add(point)
        
        if y not in self.y_axes:
            self.y_axes[y] = set()
        self.y_axes[y].add(point)
        

    def count(self, point) -> int:
        point = tuple(point)
        
        x_start, y_start = point
        
        if y_start not in self.y_axes:
            return 0
        
        points_on_y_axis = self.y_axes[y_start]
        res = 0
        
        # if you have a point
        # check all the points on it's right
        #   can they form a square?
        #       if yes, how many?
        # check all the points on it's left
        #   can they form a square?
        #       if yes, how many?
        for pos in points_on_y_axis:
            # TODO address this
            if pos == point: continue
            
            x_pos, y_pos = pos
            diff = abs(x_pos - x_start)
            
            # if the position found is on the right of the starting position
            if x_pos > x_start:
                right = (x_pos, y_start)
                right_down = (x_pos, y_start - diff)
                down = (x_start, y_start - diff)
                
                res += self.if_all_exist_get_count(right, right_down, down)
                
                right_up = (x_pos, y_start + diff)
                up = (x_start, y_start + diff)
                
                res += self.if_all_exist_get_count(right, right_up, up)
            else:
                pass
                left = (x_pos, y_start)
                left_up = (x_pos, y_start + diff)
                up = (x_start, y_start + diff)
                
                res += self.if_all_exist_get_count(left, left_up, up)
                
                left_down = (x_pos, y_start - diff)
                down = (x_start, y_start - diff)
                
                res += self.if_all_exist_get_count(left, left_down, down)
        # print(res)
        return res
                
                    
    def if_all_exist_get_count(self, two, three, four):
        res = 1
        arr = [two, three, four]
        for pos in arr:
            if pos not in self.points:
                return 0

            res *= self.points[pos]
        return res
            


sol = DetectSquares()
sol.add([3, 10])
sol.add([11, 2])
sol.add([3, 2])
sol.count([11, 10])
sol.count([14, 8])
sol.add([11, 2])
sol.count([11, 10])
