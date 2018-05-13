t=int(input())
while(t):
    a,b,c=[int(x) for x in input().split()]
    l=[a,b,c]
    l.sort()
    a,b,c=l[0],l[1],l[2]
    x=a*(a-1)*(a-2)+2*a*(a-1)*(b-a)+a*(a-1)*(c-b)+a*(b-a)*(b-a-1)+a*(b-a)*(c-b)
    print(x%1000000007)
    t-=1
