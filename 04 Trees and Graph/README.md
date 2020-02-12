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

## Tries (Prefix Trees)  
* A variant of an n-ary tree in which characters are stored at each node. Each path down the tree may
represent a word.  
* The * nodes (sometimes called "null nodes") are often used to indicate complete words.
