# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)

# Hash Table or Bool 
def palindromePermutation1(s):
    s = s.replace(" ","").lower()
    seen = set()

    for c in s:
        if c in seen:
            seen.remove(c)
        else:
            seen.add(c)
    
    return len(seen) <= 1

# Bit Vector
def palindromePermutation2(s):
    s = s.replace(" ","").lower()
    check = 0

    for c in s:
        check ^= 1<<(ord(c)-ord("a"))
    
    # notice that there should be no overlapping bit between check and check-1 if only 1 bit is 1
    return check == 0 or (check & (check-1) == 0)
