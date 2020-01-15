# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.

# EXAMPLE
# Input:
# Output:
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def append(self, x):
        n = self
        while n.next:
            n = n.next
        n.next = ListNode(x)


# recursion, time O(n), unstable
def partition1(n,x):
    if not n.next:
        return n,n
    
    first, end = partition(n.next, x)

    if n.val < x:
        n.next = first
        first = n
    else:
        end.next = n
        n.next = None
        end = n
    
    return first, end


# maintain two lists and combine, O(n), stable
def partition2(n,x):
    small = None
    big = None

    first = None
    mid = None

    while n:
        if n.val < x:
            if small:
                small.next = n
                small = small.next
            else:
                small = n
                first = n
        else:
            if big:
                big.next = n
                big = big.next
            else:
                big = n
                mid = n

        n = n.next
    
    small.next = mid
    big.next = None

    return first, big
            


# n = ListNode(3)
# n.append(5)
# n.append(8)
# n.append(5)
# n.append(10)
# n.append(2)
# n.append(1)


# n,_ = partition2(n,5)

# while n:
#     print(n.val)
#     n = n.next
