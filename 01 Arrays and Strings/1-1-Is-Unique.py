# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# Hash Table O(n)
def isUnique1(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    
    return True

# Bool Vector O(n)
def isUnique2(s):
    if len(s) > 128:
        return False
    seen = [False for i in range(128)] # ASCII str
    for c in s:
        if seen[c-'a']:
            return False
        seen[c-'a'] = True
    
    return True

# Bit Vector O(n) (assume only lowercase letter)
def isUnique3(s):
    if len(s) > 26:
        return False
    check = 0
    for c in s:
        i = ord(c) - ord('a')
        if check & (1<<i) !=0:
            return False
        
        check |= (1<<i)
    
    return True

# Sorting O(n log n ) (save memory at the price of time)
def isUnique4(s):
    s = sorted([c for c in s])
    last = None
    for c in s:
        if last == c:
            return False
        last = c
    
    return True


