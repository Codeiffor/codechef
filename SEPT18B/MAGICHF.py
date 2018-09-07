t=int(input())
while(t>0):
    n,x,s=[int(i) for i in input().split()]
    while(s>0):
        a,b=[int(i) for i in input().split()]
        if(a==x):
            x=b
        elif(b==x):
            x=a
        s-=1
    print(x)
    t-=1