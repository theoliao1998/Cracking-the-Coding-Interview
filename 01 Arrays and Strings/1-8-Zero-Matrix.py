# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

# bool vector, Space O(N)
def zeroMatrix1(M):
    row_zero = [False for _ in range(len(M))]
    col_zero = [False for _ in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 0:
                row_zero[i], col_zero[j] = True, True
    
    for i in range(len(M)):
        if row_zero[i]:
            M[i] = [0 for _ in range(len(M[0]))]
        else:
            M[i] = [0 if col_zero[j] else m for j,m in enumerate(M[i])]

# use bit vector for less space though still O(N)
def zeroMatrix2(M):
    row_zero = 0
    col_zero = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 0:
                row_zero |= (1<<i)
                col_zero |= (1<<j)
    
    for i in range(len(M)):
        if (row_zero & (1<<i)) :
            M[i] = [0 for _ in range(len(M[0]))]
        else:
            M[i] = [0 if (col_zero & (1<<j)) else m for j,m in enumerate(M[i])]

# use the first row and first col as bool vector, space O(1)
def zeroMatrix3(M):
    # check first row and first col first, since they might be changed
    row0_zero = False
    col0_zero = False
    for m in M[0]:
        if m == 0:
            row0_zero = True
            break
    
    for m in [m[0] for m in M]:
        if m == 0:
            col0_zero = True
            break
    
    for i in range(1,len(M)):
        for j in range(1,len(M[0])):
            if M[i][j] == 0:
                M[0][j], M[i][0] = 0, 0
    
    for i in range(1,len(M)):
        if M[i][0] == 0:
            M[i] = [0 for _ in range(len(M[0]))]
        else:
            M[i] = [0 if (M[0][j] == 0) and j>0 else m for j,m in enumerate(M[i])]
        
    if row0_zero:
        M[0] = [0 for _ in range(len(M[0]))]
    
    if col0_zero:
        for i in range(len(M)):
            M[i][0] = 0
