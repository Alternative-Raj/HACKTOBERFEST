for i in range(int(input())):
    s=int(input())
    m=str(input())
    n=int(m)
    k="1"*len(m)
    f=int(k,2)#maximum
    a=int(m,2)#X
    b=f-a
    n=1
    while a+int(a/2**n)!=f:
        n=n+1
    print(n)