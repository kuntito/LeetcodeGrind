# https://leetcode.com/problems/design-parking-system/description/

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.capacity = {
            1: big,
            2: medium,
            3: small,
        }
        self.parkingLot = [0, 0, 0]

    def addCar(self, carType: int) -> bool:
        slotIdx = carType - 1
        if self.parkingLot[slotIdx] < self.capacity[carType]:
            self.parkingLot[slotIdx] += 1
            return True
        
        return False
        


sol = ParkingSystem(1, 1, 0)
print(sol.addCar(1))
print(sol.addCar(2))
print(sol.addCar(3))
print(sol.addCar(1))