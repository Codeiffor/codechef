t=int(input())
for _ in range(t):
    sm=input()
    sn=input()
    m=len(sm)
    n=len(sn)
    one=False
    if(sm[0]=='1' and sn[0]=='1'):
        one=True
    
    m0=[]
    temp=0
    for i in range(m):
        if(sm[i]=='0'):
            temp=i+1
        m0.append(temp)
    
    n0=[]
    temp=0
    for i in range(n):
        if(sn[i]=='0'):
            temp=i+1
        n0.append(temp)  
    
    q=int(input())
    s=''
    for __ in range(q):
        x,y=[int(i) for i in input().split()]
        if(x>y):
            r=x-y+1
            rx=n0[r-1]
            if(rx==0 and not one):
                rx=1
            w=(x-rx+y)%2
        else:
            r=y-x+1
            ry=m0[r-1]
            if(ry==0 and not one):
                ry=1
            w=(y-ry+x)%2
        s+=str(w)
    print(s)

