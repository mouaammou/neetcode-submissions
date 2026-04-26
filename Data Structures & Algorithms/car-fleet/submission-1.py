class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        feet = []
        car_info = []
        for i in range(len(position)):
            car_info.append([position[i], speed[i]])
        
        car_info.sort(reverse=True)
        for i in range(len(car_info)):
            p, s = car_info[i]
            feet.append((target - p) / s)
            if len(feet) >= 2 and feet[-1] <= feet[-2]:
                feet.pop()
    
        return len(feet)
