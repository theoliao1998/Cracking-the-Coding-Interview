# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.

# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.

# EXAMPLE
# Input: A -> B -> C - > D -> E -> C [the same C as earlier]
# Output: C

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def append(self, x):
        n = self
        while n.next:
            n = n.next
        n.next = ListNode(x)

def loopDectection(n):

    def getLoopLength(n):
        slow, fast = n, n.next
        length = 0
        while fast:
            length += 1
            if slow == fast:
                return length
            slow = slow.next
            if not fast.next:
                return 0
            fast = fast.next.next
    
    l = getLoopLength(n)
    if not l:
        return None
    slow = n
    fast = n
    for _ in range(l):
        fast = fast.next
    
    while slow != fast:
        slow, fast = slow.next, fast.next
    
    return slow



# A = ListNode(1)
# B = ListNode(2)
# C = ListNode(3)
# D = ListNode(4)
# E = ListNode(5)

# A.next = B
# B.next = C
# C.next = D
# D.next = E
# E.next = C

# print(loopDectection(A).val)
