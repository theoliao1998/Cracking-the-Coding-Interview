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
        self.prev = None
    

class Stack:
    def __init__(self):
        self.first = None
        self.last = None
    
    def push(self, x):
        tmp = self.first
        self.first = StackNode(x)
        self.first.next = tmp
        if tmp:
            tmp.prev = self.first

    def pop(self):
        tmp = self.first
        if tmp:
            self.first = self.first.next
        if self.first:
            self.first.prev = None
        return tmp.val if tmp else None
    
    def peek(self):
        return self.first.val if self.first else None

    def isEmpty(self):
        return self.first is None

class SetOfStacks:
    def __init__(self, threshold):
        self.stacks = [Stack()]
        self.capacity = [0]
        self.threshold = threshold
    
    def push(self,x):
        if self.capacity[-1] >= self.threshold:
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
        
        self.capacity[-1] -= 1
        return self.stacks[-1].pop()
    
    def peek(self):
        tmp = self.pop()
        if tmp is None:
            return None
        self.push(tmp)
        return tmp
    
    def isEmpty(self):
        return self.peek() is None
    
    def popAt(self,n):
        if n < len(self.stacks):
            tmp = self.stacks[n].pop()
        else:
            tmp = None
        
        if tmp is not None:
            for i in range(n+1,len(self.stacks)):
                t = self.stacks[i].last
                if t is None:
                    break

                self.stacks[i-1].push(t.val)
                t.prev.next = None
                self.stacks[i].last = t.prev
                self.stacks[i].capacity -= 1
        
            if self.capacity[-1] == 0:
                self.capacity.pop()
                self.stacks.pop()
        
        return tmp

# s = SetOfStacks(3)
# for x in range(9):
#     s.push(x)

# print(s.pop())
# print(s.capacity)

# print(s.popAt(0))

# print(s.capacity)

# while not s.isEmpty():
#     print(s.pop())
                




    

