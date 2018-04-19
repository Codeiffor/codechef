n=int(input())
c=[int(x) for x in input().split()]
t=[int(x) for x in input().split()]
a1=[c[i] for i in range(0,len(c)) if(t[i]==1)]
a2=[c[i] for i in range(0,len(c)) if(t[i]==2)]
a3=[c[i] for i in range(0,len(c)) if(t[i]==3)]
if(a1==[] or a2==[]):
    print(min(a3))
elif(a3==[]):
    print(min(a1)+min(a2))
else:
    print (min(min(a1)+min(a2),min(a3)))
