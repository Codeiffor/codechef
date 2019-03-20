t = int(input())
M=1000000007
for _ in range(t):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    prod = 1
    if(k==n):
        for i in a:
            prod*=i
            prod%=M
    else:
        if(max(a)>=0):
            p=[x for x in a if x>=0]
            n=[x for x in a if x<0]
            n.sort()
            p.sort(reverse=True)
            n=[n[i]*n[i+1] for i in range(0,2*(int(len(n)/2)),2)]
            pi=0
            ni=0
            while(k):
                if(k%2==1 and len(p)-pi<=2):
                    prod*=p[pi]
                    prod%=M
                    k-=1
                    while(k):
                        prod*=n[ni]
                        prod%=M
                        ni+=1
                        k-=2
                    break
                if(len(p)==pi or(k%2==0 and len(p)==pi+1)):
                    while(k):
                        prod*=n[ni]
                        prod%=M
                        ni+=1
                        k-=2
                    break
                if(ni<len(n)):
                    if(n[ni]>p[pi]*p[pi+1]):
                        prod*=n[ni]
                        prod%=M
                        ni+=1
                    else:
                        prod*=p[pi]*p[pi+1]
                        prod%=M
                        pi+=2
                    k-=2
                else:
                    while(k):
                        prod*=p[pi]
                        prod%=M
                        pi+=1
                        k-=1
        else:
            if(k%2==0):
                a.sort()
            else:
                a.sort(reverse=True)
            for i in range(k):
                    prod*=a[i]
                    prod%=M
    print(prod)
