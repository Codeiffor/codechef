t = int(input())
for _ in range(t):
    n = int(input())
    a = [0]*32
    v=['a','e','i','o','u']

    for i in range(n):
        s=input()
        cat=''
        for j in v:
            if(j in s):
                cat+='1'
            else:
                cat+='0'
        a[int(cat,2)]+=1
    
    sum=0
    for i in range(1,32):
        for j in range(i+1,32):
            if((i|j)==31):
                sum+=a[i]*a[j]
    sum+=int(a[31]*(a[31]-1)/2)
    print(sum)