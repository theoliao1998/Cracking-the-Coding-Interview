# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed? 

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def append(self, x):
        n = self
        while n.next:
            n = n.next
        n.next = ListNode(x)

# Use Hashtable, time O(n), space O(n), one pass
def removeDups1(n):
    if not n:
        return
    prev = n
    seen = set()
    seen.add(n.val)
    while prev.next:
        if prev.next.val in seen:
            prev.next = prev.next.next
        else:
            seen.add(prev.next.val)
            prev = prev.next



# check duplication of every char, time O(n^2), space O(1)
def removeDups2(n):
    current = n
    while current:
        run = current
        while run.next:
            if run.next.val == current.val:
                run.next = run.next.next
            else:
                run = run.next

        current = current.next



# n = ListNode(2)
# n.append(5)
# n.append(3)
# n.append(3)
# n.append(4)
# n.append(3)
# n.append(4)
# n.append(5)
# n.append(7)

# removeDups2(n)

# while n:
#     print(n.val)
#     n = n.next