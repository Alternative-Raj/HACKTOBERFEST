for _ in range(int(input())):
    x=int(input())
    y=input()
    j=[int(i) for i in str(y)]
    t=[]
    print(j)
    i=1
    while len(j)!=0:
        for n in range(2): 
            if i%2!=0:
                if j[0]==0:
                    t.insert(0,j[0])
                elif j[0]==1:
                    if len(t)!=0:
                        t.insert(len(t)-1,j[0])
                    else:
                        t.insert(len(t),j[0])
                j.pop(0)
            elif i%2==0:
                if j[len(j)-1]==0:
                    t.insert(len(t)-1,j[len(j)-1])
                elif j[len(j)-1]==1:
                    t.insert(0,j[len(j)-1])
                j.pop(len(j)-1)
            i=i+1
    print(t)
        
