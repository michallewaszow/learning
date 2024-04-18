from typing import List

class MinStack:

    def __init__(self):
        self.stack: List[int] = []
        self.min_stack: List[int] = []
        # we could also use self.stack = List[List[int]] where element = [value][current_min_value]

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = val if (len(self.min_stack) == 0 or val <= self.min_stack[-1]) else self.min_stack[-1]
        # min_val = min(val, self.min_stack[-1] if self.min_stack else val) cleaner but using built-in
        self.min_stack.append(min_val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]