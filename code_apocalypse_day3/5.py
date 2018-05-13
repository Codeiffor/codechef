n,k=[int(x) for x in input().split()]
x=['a','b','c']
for i in range(3,36):
    x.append(x[i-1]+x[i-2]+x[i-3])
if(len(x[n])<k):
    print('-1')
else:
    print(x[n][k-1])
