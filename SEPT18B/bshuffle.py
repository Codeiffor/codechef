n=int(input())
s=""
for i in range(2,n//2+1):
    s+=str(i)+" "
s+='1 '
for i in range(n//2+2,n+1):
    s+=str(i)+" "
if(n!=1):
    s+=str(n//2+1)
print(s)

s=str(n)+" "
for i in range(n-1):
    s+=str(i+1)+" "
print(s)