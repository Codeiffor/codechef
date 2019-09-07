t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [2 * a[i] - b[i] for i in range(len(a))]
    print(max(max(c)*10, 0))
