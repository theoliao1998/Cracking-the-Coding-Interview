# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# lnput:the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e- >f

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, n):
        self.first = n
    
    def append(self, x):
        n = self.first
        while n.next:
            n = n.next
        n.next = ListNode(x)
    
    def print(self):
        n = self.first
        while(n):
            print(n.val)
            n = n.next

# Copy next node to current one, time O(n), cannot work if given the last node
def delMidNode(n):
    while n.next:
        n.val = n.next.val
        if n.next.next:
            n = n.next
        else:
            n.next = None
            break


# L = LinkedList(ListNode(2))
# L.append(3)
# L.append(4)
# L.append(12)
# L.append(1)

# delMidNode(L.first.next.next)
# L.print()

    