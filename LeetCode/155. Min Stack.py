# solution
class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            cur_min = min(val, self.getMin())
            self.stack.append((val, cur_min))

    def pop(self) -> None:
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
