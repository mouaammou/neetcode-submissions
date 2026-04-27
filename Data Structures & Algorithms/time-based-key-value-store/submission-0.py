class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append((timestamp, value))
        # print(self.key_store)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_store:
            return ""
        values = self.key_store[key]
        
        res = "" 
        for t, v in values:
            if t <= timestamp:
                res = v
        return res

        