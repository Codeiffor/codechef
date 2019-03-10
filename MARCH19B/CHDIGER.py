t=int(input())
for _ in range(t):
    n,d=[int(x) for x in input().split()]
    a=list(str(n))[::-1]
    a=[int(x)for x in a]
    b=[a[0]]
    for i in range(1,len(a)):
        if(a[i]<=b[-1]):
            b.append(a[i])
    b=b[::-1]+[d]*(len(a)-len(b))
    for i in range(len(b)):
        if(b[i]>d):
            b[i]=d
        b[i]=str(b[i])
    print(''.join(b))
    