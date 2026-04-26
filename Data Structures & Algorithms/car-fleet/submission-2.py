class Solution:
    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    #     feet = []
    #     car_info = []
    #     for i in range(len(position)):
    #         car_info.append([position[i], speed[i]])
        
    #     car_info.sort(reverse=True)
    #     for i in range(len(car_info)):
    #         p, s = car_info[i]
    #         feet.append((target - p) / s)
    #         if len(feet) >= 2 and feet[-1] <= feet[-2]:
    #             feet.pop()
    
    #     return len(feet)

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_info = []
        for i in range(len(position)):
            car_info.append([position[i], speed[i]])
        
        car_info.sort(reverse=True)
        current_time = (target - car_info[0][0]) / car_info[0][1]
        fleet = 1
        for i in range(1, len(car_info)):
            p, s = car_info[i]
            next_time = (target - p) / s
            if next_time > current_time:
                fleet += 1
                current_time = next_time
    
        return fleet
