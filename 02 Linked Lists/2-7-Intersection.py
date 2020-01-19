# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
# node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def append(self, x):
        n = self
        while n.next:
            n = n.next
        n.next = ListNode(x)

# first check whether intersect by comparing tail node
# then if the shorter length is l, comparing the last l node one by one
# time O(n), space O(1)
def intersectNode(n1,n2):

    # check whether intersect and get length
    def tailAndLength(n):
        if not n:
            return None, 0 
        l = 1
        while n.next:
            l += 1
            n = n.next
        
        return n, l
    
    tail1, l1 = tailAndLength(n1)
    tail2, l2 = tailAndLength(n2)
    if tail1 != tail2:
        return False, None

    if l1 < l2:
        n1, n2, l1, l2 = n2, n1, l2, l1

    for _ in range(l1-l2):
        n1 = n1.next
    
    while n1 != n2:
        n1, n2 = n1.next, n2.next
    
    return True, n1

# m = ListNode(9)
# m.append(7)
# m.append(1)
# m.append(7)
# m.append(9)

# n = ListNode(3)
# # n.next = m
# n.append(11)

# print(intersectNode(m,n))
