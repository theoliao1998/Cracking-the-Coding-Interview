# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
# to create a binary search tree with minimal height.

class Node(object):
    def __init__(self, val = 0, left = None, right = None):
        self.value = val
        self.left = left
        self.right = right
    
    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        if self.left is not None:
            ret += self.left.__repr__(level+1)
        if self.right is not None:
            ret += self.right.__repr__(level+1)
        return ret


def minTree(arr):

    def build(root,left_arr,right_arr):
        if left_arr:
            root.left = Node(left_arr[len(left_arr)//2])
            build(root.left, left_arr[:len(left_arr)//2],left_arr[len(left_arr)//2+1:])
        if right_arr:
            root.right = Node(right_arr[len(right_arr)//2])
            build(root.right, right_arr[:len(right_arr)//2],right_arr[len(right_arr)//2+1:])

    if not arr: return None
    root = Node(arr[len(arr)//2])
    build(root,arr[:len(arr)//2],arr[len(arr)//2+1:])
    return root


# s = [0,1,2,3,4,5,6,7]
# a = minTree(s)

# print(a)



