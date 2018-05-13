n,k=[int(x) for x in input().split()]
temp=str(n)
l1=temp.count('9')
l=len(str(n))
a='1'+'0'*(l-1)
a=int(a,2)
if(l==l1 and (k==1 or k==2 or k==4 or k==5 or k==7 or k==8)):
    print(str(k)*(l1*9))
else:
    k=str(k)
    while(True):
        x="{0:b}".format(a)
        x=x.replace('1',k)
        x=int(x)
        if(x>=n and x%n==0):
            print(x)
            break
        a+=1
