class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []

        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        left = 0
        right = len(self.data[key]) - 1
        # print(self.data[key])
        res = None
        while left <= right:
            mid = (left + right) // 2

            mid_value = self.data[key][mid][0]
            if mid_value == timestamp:
                return self.data[key][mid][1]
            elif mid_value <= timestamp:
                res = self.data[key][mid]
                left = mid + 1
            else:
                right = mid - 1

        return res[1] if res else ""
            