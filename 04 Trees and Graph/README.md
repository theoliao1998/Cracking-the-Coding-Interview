## Binary Search Tree  
A binary search tree is a binary tree in which every node fits a specific ordering property: all left
descendents <= n < all right descendents. This must be true for each node n.  

## Balanced vs. Unbalanced
Balanced enough to ensure 0( log n) times for insert and find, but it's not necessarily as
balanced as it could be.  

## Complete Binary Trees  
A binary tree in which every level of the tree is fully filled, except for perhaps the last level. To the extent that the last level is filled, it is filled left to right.

## Full Binary Trees
A full binary tree is a binary tree in which every node has either zero or two children. That is, no nodes have
only one child

## Perfect Binary Trees
A perfect binary tree is one that is both full and complete. All leaf nodes will be at the same level, and this
level has the maximum number of nodes  

## Binary Tree Traversal
* In-Order Traversal: visit (often, print) the left branch, then the current node, and finally, the right branch.  
* Pre-order traversal: visit the current node before its child nodes.  
* Post-order traversal: visit the current node after its child nodes.  

## Binary Heaps (Min-Heaps and Max-Heaps)
* A min-heap is a complete binary tree (that is, totally filled other than the rightmost elements on the last
level) where each node is smaller than its children. The root, therefore, is the minimum element in the tree. Max-heap is equivalent.   
* Two key operations in min-heap: *insert* and *extract_min*, both take O(log n) time.    
  * Insert:  
    * Start by inserting the element at the bottom start by inserting the element at the bottom.  
    * Then, we "fix"the tree by swapping the new element with its parent until it's proper.    
  * Extract Minimum Element:  
    * First, we remove the minimum element and swap it with the last element in the heap (the bottommost, rightmost element).  
    * Then, we bubble down this element, swapping it the smaller one of its children until the minheap property is restored.  
![image](https://user-images.githubusercontent.com/53862461/74385126-ce64e600-4dc0-11ea-99b0-079efc452353.png)

## Tries (Prefix Trees)  
* A variant of an n-ary tree in which characters are stored at each node. Each path down the tree may
represent a word.  
* The * nodes (sometimes called "null nodes") are often used to indicate complete words. Or, we could use just a boolean flag
terminates within the "parent" node.  
* Used to store the entire (English) language for quick prefix lookups. While a hash table can quickly look up whether a string is a valid word, it cannot tell us if a string is a prefix of any valid words. A trie can do this very quickly.  
![image](https://user-images.githubusercontent.com/53862461/74385052-a5dcec00-4dc0-11ea-8be0-e26801761df3.png)

## Graphs  
* A tree is a connected graph without cycles.  
* A graph is simply a collection of nodes with edges between (some of) them.  
* Graphs can be either directed or undirected. While directed edges are like a one-way street, undirected edges are like a two-way street.  
* The graph might consist of multiple isolated subgraphs. If there is a path between every pair of vertices, it is called a "connected graph".  
* The graph can also have cycles (or not). An "acyclic graph" is one without cycles.  
* In terms of programming, there are two common ways to represent a graph.  
  * Adjacency List: Every vertex (or node) stores a list of adjacent vertices. In an undirected graph, an edge like (a, b) would be stored twice: once in a's adjacent vertices and once in b's adjacent vertices.  
  * Adjacency Matrices： An NxN boolean matrix (where N is the number of nodes), where a true value at matrix[i][j] indicates an edge from node i to node j.  

## Graph Search  
* Depth-first Search (DFS):  
  * start at the root (or another arbitrarily selected node) and explore each branch completely before moving on to the next branch.  
  * DFS is often preferred if we want to visit every node in the graph. Both will work just fine, but depth-first search is a bit simpler.  
  * Note that pre-order and other forms of tree traversal are a form of DFS. The key difference is that when implementing this algorithm for a graph, we must check if the node has been visited.  
* Breadth-first Search (BFS):  
  * start at the root (or another arbitrarily selected node) and explore each neighbor before going on to any of their children.  
  * if we want to find the shortest path (or just any path) between two nodes, BFS is generally better  
  * BFS is not recursive. Instead, it uses a queue.  
* Bidirectional Search: 
  * Used to find the shortest path between a source and destination node.  
  * It operates by essentially running two simultaneous breadth-first searches, one from each node. When their searches
collide, we have found a path.  
  * Consider a graph where every node has at most k adjacent nodes and the shortest path from node s to node t has length d. BFS would need to search O(k^d) nodes while Bidirectional Search only O(k^(d/2)).  

