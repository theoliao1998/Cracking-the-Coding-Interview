# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).

# FOLLOW UP
# Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.

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
        self.first = self.first.next
        return tmp.val if tmp else None
    
    def peek(self):
        return self.first.val if self.first else None

    def isEmpty(self):
        return self.first is None

def SetOfStacks:
    def __init__(self,n, threshold):
        self.stacks = [Stack()]
        self.capacity = [0]
        self.threshold = threshold
    
    def push(self,x):
        if self.capacity[-1] > self.threshold:
            self.stacks.append(Stack())
            self.capacity.append(0)

        self.stacks[-1].push(x)
        self.capacity[-1] += 1
    
    def pop(self):
        if self.capacity[-1] == 0:
            if len(self.capacity) <= 1:
                return None
            self.capacity.pop()
            self.stacks.pop()
        
        self.capacity[-1] -= 1:
        return self.stacks[-1].pop()
    
    def peek(self):
        tmp = self.pop()
        if tmp is None:
            return None
        self.push(tmp)
        return tmp
    
    def isEmpty(self):
        return self.peek() is None
    
    # def popAt(self,n):
    #     if n < len(self.stacks):
    #         tmp = self.stacks[n].pop()
    #     else:
    #         tmp = None
    #     if tmp is None:
    #         return None


    

