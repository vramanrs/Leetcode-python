from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.s = size

    def next(self, val: int) -> float:
        if len(self.q) >= self.s:
            self.q.pop()
        self.q.appendleft(val)
        return sum(self.q) / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)