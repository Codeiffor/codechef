def gcd(a, b):
  while b:
    a, b = b, a % b
  return a
n,m,x=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
ac,bc=0,0
for i in a:
    if(gcd(i,x)==1):
        ac+=1
for i in b:
    if(gcd(i,x)==1):
        bc+=1
print(ac*bc)
