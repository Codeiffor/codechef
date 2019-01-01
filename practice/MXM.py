t=int(input())
for _ in range(t):
    x=input()
    a=[int(x)+1 for x in input().split()]
    x,l,r=1,0,sum(a)
    for i in range(len(a)-1):
        l+=a[i]
        r-=a[i]
        if(l<=r):
            x=i+1
        else:
            break
    print(x)
    