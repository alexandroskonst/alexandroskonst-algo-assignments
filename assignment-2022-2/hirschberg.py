import sys
import numpy as np
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
def enumerateAlignments(A, B, F, W, Z, WW, ZZ, g):
    i = len(A)
    j = len(B)

    if i==0 and j==0:
         WW.append(W)
         ZZ.append(Z)
         #print (WW)
         #print (ZZ)


    if i>0 and j>0:
        b = False
        if i == 1:
            for k in range (0,j):
                if A[0] == B[k]:
                    b = True
                    WW = ["-" for x in range(0,k)] + [A[0]] + ["-" for x in range(k+1, j)]
                    ZZ = [B[x] for x in range(0,j)]
            if not b:
                WW = [A[x] for x in range(0,i)]
                ZZ = [B[x] for x in range(0,j)]
            return WW, ZZ
        if j == 1:
            for k in range(0,i):
                if B[0] == A[k]:
                    b = True
                    WW = [A[x] for x in range(0,i)]
                    ZZ = ["-" for x in range(0,k)] + [B[0]] + ["-" for x in range(k+1, i)]
            if not b:
                WW = [A[x] for x in range(0,i)]
                ZZ = [B[x] for x in range(0,j)]
            return WW, ZZ

        m = compare(A[i-1], B[j-1])
        if F[i][j] == F[i-1][j-1] + m:
            enumerateAlignments(A[0:i-1], B[0:j-1], F, [A[i-1]] + W, [B[j-1]] + Z, WW, ZZ)
    if i > 0 and F[i][j] == F[i-1][j] + g:
            enumerateAlignments(A[0:i-1], B, F, [A[i-1]] + W, ["-"] + Z, WW, ZZ)
    if j > 0 and F[i][j] == F[i][j-1] + g:
            print(j)
            enumerateAlignments(A, B[0:j-1], F, ["-"] + W, [B[j-1]] + Z, WW, ZZ)
    return WW, ZZ



def ComputeAlignmentScore(A,B,g):
 L = [None] * (len(B)+1)
 for j in range(0, len(L)):
     L[j] = (j*g)
 K = [None] * (len(B)+1)

 for i in range(1, len(A)+1):
     L,K = K,L
     L[0] = i*g
     for j in range( 1 , len(B)+1):
         md = compare(A[i-1], B[j-1])
         L[j] = max(L[j-1] + g, K[j]+g, K[j-1] + md)

 return L


def getIndFromElement(list, max):
    l2 = []
    for x in range(0,len(list)):
        if list[x] == max:
            l2.append(x)
    return l2

def varTolist(A):
    if type(A) == list:
        return A
    else:
        return [A]

def hirschberg(A, B, g, t):
    if len(A) == 0:
        WW = "-" * len(B)
        ZZ = B
    elif len(B) == 0:
        WW = A
        ZZ = "-" * len(A)
    elif len(A) == 1 or len(B) == 1:
        F = ComputeAlignmentScore(A, B, g)
        WW, ZZ = enumerateAlignments(A, B, F, [], [], [], [], g)
    else:
        i = int(np.floor(len(A) / 2))
        Sl = ComputeAlignmentScore(A[0:i], B, g)
        Ar = A[i:len(A)][::-1]
        Br = B[::-1]
        Sr = ComputeAlignmentScore(Ar, Br, g)

        S = [a + b for a, b in zip(Sl, Sr[::-1])]
        maxx = max(S)
        J = getIndFromElement(S, maxx)
        WW = list()
        ZZ = list()
        for j in J:
            if t:
                print(i, j)

            WWl, ZZl = hirschberg(A[0:i], B[0:j], g, t)
            WWr, ZZr = hirschberg(A[i:len(A)], B[j:len(B)], g, t)

            WWl = varTolist(WWl)
            WWr = varTolist(WWr)
            ZZl = varTolist(ZZl)
            ZZr = varTolist(ZZr)

            WW.append(WWl + WWr)

            ZZ.append(ZZl + ZZr)
    WW = [item for sublist in WW for item in sublist]
    ZZ = [item for sublist in ZZ for item in sublist]
    return WW, ZZ

def run():
    args = []
    for arg in sys.argv:
        args.append[arg]

    t = False
    f = False
    l = False

    if '-t' in args:
        t = True
    if '-f' in args:
        f = True #files
    if '-l' in args:
        l = True
    B = args[-1]
    A = args[-2]
    d = args[-3]
    m = args[-4]
    g = args[-5]
    X, Y = hirschberg(A, B, g, t)
    print(X, Y)

run()

#A = 'GACGC'
#B = 'ACTGACG'
#X, Y = hirschberg(A, B, g, t)
#print(X, Y)
