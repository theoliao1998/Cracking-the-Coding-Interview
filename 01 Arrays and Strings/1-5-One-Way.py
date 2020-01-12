# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false


def oneWay(s1, s2):
    if len(s2) > len(s1):
        s1, s2 = s2, s1
        # s1 ^= s2
        # s2 ^= s1
        # s1 ^= s2
    
    check = len(s1) - len(s2)

    if check > 1:
        return False
    
    i,j = 0,0
    once = False

    while j < len(s2):
        if s1[i] != s2[j]:
            if once: return False
            once = True
            if check:
                i += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    if i < len(s1) and once:
        return False
    return True
