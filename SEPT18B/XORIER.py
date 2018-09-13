import operator
def cc(n):
    return n*(n-1)//2
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    a.sort()
    e=[]
    ecnt=[]
    o=[]
    ocnt=[]
    for x in a:
        if(x%2==0):
            if(e and e[-1]==x):
                ecnt[-1]+=1
            else:
                e.append(x)
                ecnt.append(1)
        else:
            if(o and o[-1]==x):
                ocnt[-1]+=1
            else:
                o.append(x)
                ocnt.append(1)

    el=len(e)
    ol=len(o)
    ec=cc(sum(ecnt))
    oc=cc(sum(ocnt))
    r=0

    for i in range(el):
        for j in range(i+1,el):
            if(e[j]-e[i]>3):
                break
            if(operator.xor(e[j],e[i])<4):
                r+=ecnt[i]*ecnt[j]
    for i in range(ol):
        for j in range(i+1,ol):
            if(o[j]-o[i]>3):
                break
            if(operator.xor(o[j],o[i])<4):
                r+=ocnt[i]*ocnt[j]
    
    for i in range(el):
        if(ecnt[i]>1):
            r+=cc(ecnt[i])
    for i in range(ol):
        if(ocnt[i]>1):
            r+=cc(ocnt[i])

    print(ec+oc-r)

