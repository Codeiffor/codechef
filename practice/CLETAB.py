def replaceTable(orders,tables,x,n):
    occ=[-1]*n
    for i in range(n):
        if(tables[i] in orders[x+1:]):
            occ[i] = orders[x+1:].index(tables[i])
    if (-1 in occ):
        return occ.index(-1)
    else:
        return occ.index(max(occ))

t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    orders = [a[0]]
    for i in range(1, m):
        if(a[i] != a[i-1]):
            orders.append(a[i])
    m = len(orders)

    tables = []

    count = 0
    for i in range(m):
        if(orders[i] in tables):
            continue
        if(len(tables) < n):
            tables.append(orders[i])
        else:
            j=replaceTable(orders,tables,i,n)
            tables[j]=orders[i]
        count += 1
    
    print(count)