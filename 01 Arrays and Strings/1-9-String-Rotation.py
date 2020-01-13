# String Rotation:Assume you have a method isSubstringwhich checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").

def isSubstring(s1,s2):
    return s1 in s2

def isRotation(s1,s2):
    if len(s1) != len(s2):
        return False
    s2 += s2
    return isSubstring(s1,s2)
