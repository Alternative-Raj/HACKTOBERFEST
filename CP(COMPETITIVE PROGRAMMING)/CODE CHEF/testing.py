import random as rm

def lcs(X, Y, m, n): 
    if m == 0 or n == 0: 
        return 0
    elif X[m-1] == Y[n-1]: 
        return 1 + lcs(X, Y, m-1, n-1); 
    else: 
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))
def lcs2(a,b,v):
    o=0
    k=0
    for z in range(v):
        if a[z]==b[z]:
            k=k+1
        if a[z] in b:
            o=o+1
    if k==0:
        print(o)
    else:
        print(k)
for i in range(int(input())):
    v=int(input())
    a=input()
    b=input()
    print ( lcs(a , b, len(a), len(b)) )
    lcs2(a,b,v)