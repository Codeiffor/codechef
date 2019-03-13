t = int(input())
for _ in range(t):
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    
    for _ in range(n):
        arr=[a[_]]
        c=[0]*2001
        l=0
        for i in range(_,n):
            if(i!=_):
                st=0
                end=l-1
                while(st<=end):
                    mid=int((st+end)/2)
                    if(mid==l-1):
                        break
                    if(arr[mid]==a[i]):
                        break
                    if(arr[mid]<a[i] and arr[mid+1]>a[i]):
                        mid+=1
                        break
                    if(arr[mid]>a[i]):
                        end=mid-1
                        continue
                    if(arr[mid]<a[i]):
                        st=mid+1
                        continue
                if(mid==0 or mid==l-1):
                    if(a[i]>arr[mid]):
                        mid+=1
                arr.insert(mid, a[i])                
            c[a[i]]+=1
            l+=1

            print(arr)

