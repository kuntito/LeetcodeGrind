class Solution:
    def wateringPlants(self, plants: list[int], capacity: int) -> int:
        curr_capacity = capacity
        steps = 0

        for idx, water_need in enumerate(plants):
            pass
            curr_capacity -= water_need

            next_idx = idx + 1
            if next_idx < len(plants) and curr_capacity < plants[next_idx]:
                curr_capacity = capacity
                steps_to_go_back = (idx + 1) * 2
                steps += steps_to_go_back

            steps += 1

        return steps
    

plants, capacity = [5,2,4,2,7,4,3,3,1,1], 10
sol = Solution()
res = sol.wateringPlants(plants, capacity)
print(res)
