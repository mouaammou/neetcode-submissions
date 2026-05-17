class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        data = list(zip(position, speed))
        data.sort(reverse=True)

        last_time = 0
        fleet = 0

        for p, s in data:
            time = (target - p) / s
            if time > last_time:
                fleet += 1
                last_time = time

        return fleet