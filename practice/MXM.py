t=int(input())
for _ in range(t):
    x=input()
    a=[int(x)+1 for x in input().split()]
    x,l=1,0
    r=1
    for tmp in a:
        r*=tmp
    for i in range(len(a)-1):
        l*=a[i]
        r/=a[i]
        if(l<=r):
            x=i+1
        else:
            break
    print(x)
    