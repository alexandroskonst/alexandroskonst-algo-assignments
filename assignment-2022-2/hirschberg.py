import sys
sys.setrecursionlimit(10000)

def compare(x,y):
    m = 1
    d = -1

    if x==y:
        return m 
    else:
        return d 

A = 'GACGC'
B = 'ACTGACG'
F = [[0, -2, -4, -6, -8, -10, -12, -14], [-2, -1, -3, -5, -5, -7, -9, -11], [-4, -1, -2, -4 ,-6, -4, -6, -8], [-6, -3, 0, -2, -4, -6, -3, -5 ], [-8, -5, -2, -1, -1, -3, -5, -2], [-10, -7, -4, -3, -2, -2, -2, -4]]
W = list()
Z = list()
WW = []
ZZ = []
def enumerateAlignments(A, B, F, W, Z, WW, ZZ):
    g = -2
    i = len(A)
    j = len(B)
    
    if i==0 and j==0:
         WW.append(W)
         ZZ.append(Z)
         print (WW)
         print (ZZ)
         
         
    if i>0 and j>0:
        m = compare(A[i-1], B[j-1])
        if F[i][j] == F[i-1][j-1] + m:
            enumerateAlignments(A[0:i-1], B[0:j-1], F, [A[i-1]] + W, [B[j-1]] + Z, WW, ZZ)
    if i > 0 and F[i][j] == F[i-1][j] + g:
            enumerateAlignments(A[0:i-1], B, F, [A[i-1]] + W, ["-"] + Z, WW, ZZ)
    if j > 0 and F[i][j] == F[i][j-1] + g:
            print(j)
            enumerateAlignments(A, B[0:j-1], F, ["-"] + W, [B[j-1]] + Z, WW, ZZ)
    return WW, ZZ
enumerateAlignments(A,B,F,W,Z, WW, ZZ)



    