
## Hash Tables  
* Implement with linked list  
![ll](https://user-images.githubusercontent.com/53862461/72211488-1f1fb100-349a-11ea-9f13-574b564189a9.PNG)  
  * Worst case runtime is O(N), where N is the number of keys.
  * Assume a good implementation that keeps collisions to a minimum, the lookup time is O(1).  
* Implement with a balanced binary search tree.  
![BSTSearch](https://user-images.githubusercontent.com/53862461/72211523-d288a580-349a-11ea-90e0-0ff0b97ebc1e.png)  
  * O(log N) lookup time.  
  * Less space, since we no longer allocate the hash value sized array.  
  * We can also iterate through the keys in order.  

## Arraylist & Resizable Arrays  
* When the array is full, the array doubles in size.  
* Each doubling takes O(n) time, on average O(1) for an insertion.  

## StringBuilder  
* When concatenating a list of strings of size x, concatenating one by one would require O(x+2x+3x+...+nx)=O(n^2 x) time.
* StringBuilder simply creates a resizable array of all the strings, copying them back to a string only when necessary.  
* O(n) for insertion, plus O(nx) for copying back together.  
