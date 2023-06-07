class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, value):
        self.stack.append(value)
        if not self.maxStack or value >= self.maxStack[-1]:
            self.maxStack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.maxStack[-1]:
            self.maxStack.pop()
        return value

    def getMax(self):
        if not self.maxStack:
            return None
        return self.maxStack[-1]
max_stack = MaxStack()

max_stack.push(5)
max_stack.push(8)
max_stack.push(3)

print(max_stack.getMax())  # Output: 8

max_stack.push(12)
print(max_stack.getMax()) # output 12
print(max_stack.pop())     # Output: 12

print(max_stack.getMax())  # Output: 8

print(max_stack.pop())     # Output: 3

print(max_stack.getMax())  # Output: 8
print(max_stack.pop()) # output 8
print(max_stack.getMax()) #output 5