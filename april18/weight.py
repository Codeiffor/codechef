m=1000000007
p=[10]
for i in range(1,19):
    p.append((p[i-1]**10)%m)
t=int(input())
while(t):
    n,w=input().split()
    n,w=int(n),int(w)
    y=n-2
    i=18
    x=1
    while(i>=0  and y>0):
        z=10**i
        while(y-z>=0):
            y-=z
            x=(x*p[i])%m
        i-=1
    if(w>8 or w<-9):
        x=0
    elif(w>=0):
        x=((9-w)*x)%m
    else:
        x=(x*(10+w))%m
    print(x)
    t-=1
