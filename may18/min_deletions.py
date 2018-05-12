t=int(input())
from fractions import gcd
while(t>0):
    n=int(input())
    a=[int(x)for x in input().split()]
    ans=-1
    x=gcd(a[0],a[1])
    for i in range(1,len(a)):
        x=gcd(a[i],x)
        if(x==1):
            ans=0
            break
    print(ans)
    t-=1
