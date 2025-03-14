# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    # create an array with integers `[big, medium, small]`, `carPark`
    # convert each car to an index with `carType - 1`
    
    # if carPark[0] is truthy, decrement that index `carPark[idx] -= 1`
    #   return True
    # else return False
    def __init__(self, big: int, medium: int, small: int):
        pass
        self.carPark = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        idx = carType - 1
        
        if self.carPark[idx]:
            self.carPark[idx] -= 1
            return True
            
        return False