# Palindrome: Implement a function to check if a linked list is a palindrome.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def append(self, x):
        n = self
        while n.next:
            n = n.next
        n.next = ListNode(x)

# recursion, time O(n), space O(n), similarly we can use a stack
def palindrome1(n):
    if not n:
        return True
    
    def midNode(n):
        slow = n
        fast = n
        while fast:
            if not fast.next:
                return slow, slow
            if not fast.next.next:
                return slow, slow.next
            slow = slow.next
            fast = fast.next.next
    
    mid1,mid2 = midNode(n)
    if mid1.val != mid2.val:
        return False

    def checkPalindrome(n,mid1,mid2):
        if n == mid1:
            return True, mid2.next
        
        judge, compare = checkPalindrome(n.next, mid1, mid2)
        return judge and n.val == compare.val, compare.next

    return checkPalindrome(n,mid1,mid2)[0]

# reverse and compare, time O(n), space O(n)
def palindrome2(n):

    def reverse(n):
        head = ListNode(n.val)
        while(n.next):
            tmp = ListNode(n.next.val)
            tmp.next = head
            head = tmp
            n = n.next
        
        return head
    
    def compare(a,b):
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        
        if a or b:
            return False
        
        return True
    
    return compare(n,reverse(n))

# m = ListNode(9)
# m.append(7)
# m.append(1)
# m.append(7)
# m.append(9)

# print(palindrome2(m))

        
