# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


# inplace rotate layer by layer outside in O(n^2)
def rotateMatrix(M):
    for i in range((len(M)+1)//2):
        for j in range(i,len(M)-i-1):
            M[i][j],M[j][-i-1],M[-i-1][-j-1],M[-j-1][i] = M[-j-1][i],M[i][j],M[j][-i-1],M[-i-1][-j-1]
