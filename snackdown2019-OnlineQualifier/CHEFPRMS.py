prime=[]
for i in range(2,100):
    p=True
    for j in range(2,int(pow(i,0.5))+1):
        if(i%j==0):
            p=False
            break
    if(p):
        prime.append(i)
semiprime=[]
for i in range(len(prime)):
    for j in range(i+1,len(prime)):
        if(prime[i]*prime[j]>200):
            break
        semiprime.append(prime[i]*prime[j])
semiprime.sort()
sumsemiprime=[]
for i in range(len(semiprime)):
    for j in range(i,len(semiprime)):
        if(semiprime[i]+semiprime[j]>200):
            break
        sumsemiprime.append(semiprime[i]+semiprime[j])
        
t=int(input())
for _ in range(t):
    n=int(input())
    if(n in sumsemiprime):
        print("YES")
    else:
        print("NO")