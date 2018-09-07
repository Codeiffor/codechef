t=int(input())
while(t>0):
    n,m,x,y=[int(i) for i in input().split()]
    if( ( ( (n-1)%x==0 and (m-1)%y==0 )or( (n-2)%x==0 and (m-2)%y==0 ) ) and n>1 and m>1 ):
        print("Chefirnemo")
    elif( ( (n-1)%x==0 and (m-1)%y==0 ) and (n==1 or m==1) ):
        print("Chefirnemo")
    else:
        print("Pofik")
    t-=1