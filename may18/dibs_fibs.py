M=1000000007
fib_count=[(1,0),(0,1)]
for i in range(2,100001):
    fib_count.append(((fib_count[i-1][0]+fib_count[i-2][0])%M,(fib_count[i-1][1]+fib_count[i-2][1])%M))
###
t=int(input())
while(t>0):
    m,n=[int(x)for x in input().split()]
    a=[int(x)for x in input().split()]
    b=[int(x)for x in input().split()]
    result=0
    for i in range(m):
        result+=(a[i]*fib_count[n-1][0]+b[i]*fib_count[n-1][1])%M
    result*=m
    print(result%M)
    t-=1
