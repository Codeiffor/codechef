t=int(input())
while(t>0):
    s,n=input().split()
    n=int(n)
    x=0
    w=[]
    for i in range(0,len(s)):
        if(s[i]=='a'):
            x+=1
        else:
            x-=1
        w.append(x)
    ans=0
    if(x==0):
        for i in range(0,len(s)):
            if(w[i]>0):
                ans+=n
    elif(x<0):
        for i in range(0,len(s)):
            temp=0
            if(w[i]>0):
                temp=int(w[i]/(-x))
                if(w[i]%(-x)!=0):
                    temp+=1
            ans+=min(temp,n)
    else:
        for i in range(0,len(s)):
            temp=0
            if(w[i]<=0):
                temp=int((-w[i])/x)+1
            ans+=max(n-temp,0)
    print(ans)
    t-=1
