n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    if 1<x<4 and 1<y<4:
        print(2,2)
    else:
        print(x,y)