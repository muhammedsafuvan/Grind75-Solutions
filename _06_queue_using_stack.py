from collections import deque


class MyQueue:

    def __init__(self):
        self.data = deque()
        

    def push(self, x: int) -> None:
        self.data.appendleft(x)
        

    def pop(self) -> int:
        return self.data.pop()
        

    def peek(self) -> int:
        return self.data[-1]
        

    def empty(self) -> bool:
        return len(self.data) == 0
        