n, x, y = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [[a[i]-b[i], max(a[i], b[i]), min(a[i], b[i])] for i in range(n)]
c.sort(reverse=True, key=lambda x: (x[2]))
c.sort(reverse=True, key=lambda x: (x[1]))
c.sort(reverse=True, key=lambda x: abs(x[0]))

sum=0
for i in range(n):
    if(c[i][0]==0):
        sum+=c[i][1]
    elif(c[i][0]>0):
        if(x>0):
            sum+=c[i][1]
            x-=1
        else:
            # j=i
            # while(j>0):
            #     if(c[j-1][0]>0 and c[j-1][1]==c[j][1] and c[j-1][3]==False):
            #         j-=1
            #     else:
            #         break
            sum+=c[i][2]
            y-=1
            # c[j][3]=True
    else:
        if(y>0):
            sum+=c[i][1]
            y-=1
        else:
            # j=i
            # while(j>0):
            #     if(c[j-1][0]<0 and c[j-1][1]==c[j][1] and c[j-1][3]==False):
            #         j-=1
            #     else:
            #         break
            sum+=c[i][2]
            x-=1
            # c[j][3]=True


# print(c)
print(sum)