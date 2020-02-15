# Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.

from queue import Queue

class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
        self.visited = False

def BFS(A,B):
    queue = Queue()
    cur = A
    while cur is not None and cur != B:
        if cur.visited == False:
            cur.visited = True
            for node in cur.neighbors:
                queue.put(node)
        
        cur = None if queue.empty() else queue.get()
    
    return cur is not None and cur == B

def DFS(A,B):
    if A == B:
        return True
    
    A.visited = True
    for node in A.neighbors:
        if not node.visited:
            if DFS(node,B):
                return True
    
    return False


# A = Node(1)

# B = Node(2)

# C = Node(3)

# A.neighbors = [B]

# B.neighbors = [A]

# print(BFS(A,C))
