class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
    

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            min_elem = min(self.min_stack[-1], val)
            self.min_stack.append(min_elem)            

            
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        # if self.min_stack:append
        


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
