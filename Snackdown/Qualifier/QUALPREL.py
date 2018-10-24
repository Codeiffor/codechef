t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    kl = [int(x) for x in input().split()]
    kl = sorted(kl, reverse = True)
    score = kl[k-1]
    count = 0
    for j in kl:
        if j>=score:
            count+=1
        else:
            break
    print(count)
