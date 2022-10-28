n=int(input())
for i in range(n):
    a,b,x=map(int,input().split())
    if ((a-b)%x==0) and (b+a)%x==0:
        print('YES')
    elif a==b:
        print("YES")
    else:
        print("NO")
        