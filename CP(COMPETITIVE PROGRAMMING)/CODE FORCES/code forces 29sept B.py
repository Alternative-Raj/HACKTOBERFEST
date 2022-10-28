n=int(input())
for i in range(n):
    l=int(input())
    d=map(int,input().split())
    c=[]
    c.extend(d)
    a=[]
    a.append(c[0])
    for j in range(1,l):
        if a[j-1]>=c[j]:
            a.append(a[j-1]+c[j])
            if j==l-1:
                print(str(a))
        #else:
            #print(-1)
            #break
        print(j)
        

