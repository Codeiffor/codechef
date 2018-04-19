t=int(input())
while(t>0):
    n=int(input())
    c=[0 for i in range(-1000,1001)]
    a=[int(x) for x in input().split()]
    for i in a:
        c[i+1000]+=1
    #l=[x for x in range(-1000,1001)]
    cnt=0
    for i in range(-1000,1001):
        if(c[i+1000]==0):
            continue
        x,y=i,i
        while(x>=-1000 and y<=1000):
            if(x==y):
                cnt+=int(c[x+1000]*(c[x+1000]-1)/2)
            else:
                cnt+=c[x+1000]*c[y+1000]
            x,y=x-1,y+1
    print(cnt)
    t-=1
