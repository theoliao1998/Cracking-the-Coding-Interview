# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

class StackNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    

class Stack:
    def __init__(self):
        self.first = None

    def push(self, x):
        tmp = self.first
        self.first = StackNode(x)
        self.first.next = tmp

    def pop(self):
        tmp = self.first
        if tmp:
            self.first = self.first.next
        return tmp.val if tmp else None
    
    def peek(self):
        return self.first.val if self.first else None

    def isEmpty(self):
        return self.first is None

class MyQueue:
    def __init__(self):
        self.original = Stack()
        self.reverse = Stack()
    
    def push(self, x):
        while not self.reverse.isEmpty():
            self.original.push(self.reverse.pop())
        
        self.original.push(x)
    
    def pop(self):
        while not self.original.isEmpty():
            self.reverse.push(self.original.pop())

        return self.reverse.pop()

# a = MyQueue()
# a.push(3)
# a.push(2)
# a.push(5)

# print(a.pop())
# a.push(6)
# print(a.pop())
# print(a.pop())
# print(a.pop())