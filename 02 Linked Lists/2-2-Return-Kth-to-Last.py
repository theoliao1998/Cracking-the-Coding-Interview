# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def append(self, x):
        n = self
        while n.next:
            n = n.next
        n.next = ListNode(x)

# "Runner"Technique O(n), one pass
def kthToLast1(n,k):
    slow = n
    fast = n
    for i in range(k):
        if not fast:
            break
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow


# recursion O(n)
def kthToLast2(n,k):

    def indexToLast(n,k,res):
        if not n:
            return 0
        i = indexToLast(n.next,k,res) + 1
        if i == k:
            res[0] = n
        return i
    
    res = [None]
    indexToLast(n,k,res)
    return res[0]


# n = ListNode(2)
# n.append(5)
# n.append(3)
# n.append(3)
# n.append(4)
# n.append(3)
# n.append(4)
# n.append(5)
# n.append(7)

# print(kthToLast2(n,3).val)
