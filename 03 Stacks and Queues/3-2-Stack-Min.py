# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

class StackNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.submin = x
    

class Stack:
    def __init__(self):
        self.first = None
    
    def push(self, x):
        tmp = self.first
        self.first = StackNode(x)
        self.first.next = tmp
        self.first.submin = min(x,tmp.submin) if tmp else x
    
    def pop(self):
        tmp = self.first
        self.first = self.first.next
        return tmp.val if temp else None
    
    def peek(self):
        return self.first.val if self.first else None

    def isEmpty(self):
        return self.first is None
    
    def min_val(self):
        return self.first.submin if self.first else None
