'''We have to design a min stack class, in this just the extra function is using giving back min stack'''


class MinStack:

    def __init__(self):
        self.stack = []


    def push(self, val):
        currMin = self.getMin()
        if not currMin or currMin<val:
            currMin = val

        self.stack.append((val,currMin))

    def pop(self):
        if self.stack:
            self.stack.pop()


    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return None