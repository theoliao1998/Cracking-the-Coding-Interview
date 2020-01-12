# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

# Sort (O(n log n))
def checkPermutation1(s1, s2):
    if len(s1) != len(s2):
        return False
    
    s1 = ''.join(sorted([c for c in s1]))
    s2 = ''.join(sorted([c for c in s2]))
    return s1 == s2

# Character counts O(n)
def checkPermutation2(s1, s2):
    if len(s1) != len(s2):
        return False
    
    freq = {} # or use a list with size of 128 (ASCII)
    for c in s1:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    
    for c in s2:
        if c not in freq or freq[c] <= 0:
            return False
        freq[c] -= 1
    
    for cnt in freq.values():
        if cnt != 0:
            return False 

    return True
