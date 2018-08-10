t=int(input())
def gcd(a,b):
    while(b>0):
        a,b=b,a%b
    return a
M=1000000007
while(t>0):
    a,b,n=[int(x) for x in input().split()]
    if(a==b):
        print((pow(a,n,M)+pow(b,n,M))%M)
    else:
        print(gcd(pow(a,n,a-b)+pow(b,n,a-b),a-b)%M)
    t-=1