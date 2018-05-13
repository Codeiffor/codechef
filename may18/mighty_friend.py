t=int(input())
while(t>0):
    n,k=[int(x)for x in input().split()]
    a=[int(x)for x in input().split()]
    odd=[a[i]for i in range(0,n)if(i%2==0)]
    even=[a[i]for i in range(0,n)if(i%2==1)]
    odd.sort()
    even.sort()
    odd.reverse()
    diff=sum(odd)-sum(even)
    x=0
    while(diff>=0 and x<k):
        if(odd[x]-even[x]<=0):break
        diff-=(odd[x]-even[x])*2
        x+=1
    if(diff<0):print('YES')
    else:print('NO')
    t-=1
