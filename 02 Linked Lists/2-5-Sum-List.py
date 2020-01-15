# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.

# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def append(self, x):
        n = self
        while n.next:
            n = n.next
        n.next = ListNode(x)

# add digit by digit, O(n)
def sumList(m,n):
    m_val = m.val if m else 0
    n_val = n.val if n else 0
    res = ListNode((m_val+n_val)%10)
    carry = 1 if (m_val+n_val) >= 10 else 0
    if m: m = m.next
    if n: n = n.next
    cur = res

    while m or n:
        m_val = m.val if m else 0
        n_val = n.val if n else 0
        cur.next = ListNode((m_val+n_val+carry)%10)
        carry = 1 if (m_val+n_val+carry) >= 10 else 0
        if m: m = m.next
        if n: n = n.next
        cur = cur.next
    

    if carry:
        cur.next = ListNode(1)
    
    return res

# m = ListNode(1)
# m.append(7)
# m.append(8)
# m.append(6)

# n = ListNode(5)
# n.append(9)
# n.append(2)

# res = sumList(m,n)

# while res:
#     print(res.val)
#     res = res.next


# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
# Output: 9 - > 1 -> 2. That is, 912


def sumListForward(m,n):

    def length(l):
        res = 0
        while l:
            res += 1
            l = l.next
        
        return res
    
    def add(m,n,res):
        if not m.next:
            res.val = (m.val+n.val)%10
            return 1 if (m.val+n.val) >= 10 else 0
        
        res.next = ListNode(None)
        value = m.val + n.val + add(m.next,n.next,res.next)
        res.val = value % 10
        return 1 if value >= 10 else 0
    
    l1, l2 = length(m), length(n)

    if l1 < l2:
        m,n,l1,l2 = n,m,l2,l1
    
    for _ in range(l1-l2):
        tmp = ListNode(0)
        tmp.next = n
        n = tmp

    res = ListNode(None)

    if add(m,n,res):
        tmp = ListNode(1)
        tmp.next = res
        res = tmp
    
    return res

# m = ListNode(9)
# m.append(7)
# m.append(1)
# m.append(9)

# n = ListNode(5)
# n.append(9)
# n.append(9)

# res = sumListForward(m,n)

# while res:
#     print(res.val)
#     res = res.next







