t=int(input())
while(t>0):
    n=int(input())
    a=[int(x)for x in input().split()]
    ans=0
    for i in a:
        ans^=2*i
    print(ans)
    t-=1
