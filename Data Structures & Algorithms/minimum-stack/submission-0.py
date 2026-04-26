class MinStack:

    def __init__(self):
        self.stack = []
        self.track_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.track_min.append(val)
        if len(self.track_min) >= 2:
            if self.track_min[-2] < val:
                self.track_min[-1] = self.track_min[-2]

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.track_min.pop()

    def top(self) -> int:
        # if self.stack:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 1:
            return self.stack[0]
        return self.track_min[-1]
