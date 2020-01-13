# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

# Brute Force O(n^2) since str concat every iteration
def stringCompression1(s):
    last = None
    cnt = 0
    res = ""
    for c in s:
        if c == last:
            cnt += 1
        else:
            if last:
                res += last + str(cnt)
                if len(res) >= len(s):
                    return s
            
            last = c
            cnt = 1
    
    if last:
        res += last + str(cnt)
        if len(res) >= len(s):
            return s

    return res

# string builder O(n)
def stringCompression2(s):
    last = None
    cnt = 0
    res = []
    l = 0
    for c in s:
        if c == last:
            cnt += 1
        else:
            if last:
                res += [last[0], str(cnt)]
                l += len(res[-1])+1
                if l >= len(s):
                    return s
            
            last = c
            cnt = 1
    
    if last:
        res += [last[0], str(cnt)]
        l += len(res[-1])+1
        if l >= len(s):
            return s

    return "".join(res)
