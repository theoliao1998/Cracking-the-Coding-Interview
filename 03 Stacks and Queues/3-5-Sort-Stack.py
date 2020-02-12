# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.

# if not limit of additional stacks, we can use quicksort and mergesort (based on stacks)

class StackNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    

class Stack:
    def __init__(self):
        self.first = None

    def push(self, x):
        if x is None:
            return
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

# O(n^2) time and O(n) space (Consider the worst case: n + (n-1) + ... + 2 + 1 times pop and push)
def sortStack(s):
    tmpStack = Stack()
    tmpStack.push(s.pop())
    while not s.isEmpty():
        tmp = s.pop()
        while tmpStack.peek() is not None and tmpStack.peek() > tmp:
            s.push(tmpStack.pop())
        tmpStack.push(tmp)
    
    while not tmpStack.isEmpty():
        s.push(tmpStack.pop())

# s = Stack()
# s.push(7)
# s.push(3)
# s.push(19)
# s.push(22)
# s.push(0)
# s.push(17)
# s.push(7)
# sortStack(s)

# while not s.isEmpty():
#     print(s.pop())