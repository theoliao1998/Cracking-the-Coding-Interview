
* Unlike an array, reuqires O(n) time to index rather than O(1)  

## The "Runner"Technique  
* Iterate through the linked list with two pointers simultaneously, with one ahead of the other.  
* The "fast" node might be ahead by a fixed amount, or it might be hopping multiple nodes for each
one node that the "slow" node iterates through.  
