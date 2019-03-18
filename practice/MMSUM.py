t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    maxsum = max(a)
    _sum = 0
    dropped = 0
    rsum = 0
    pin = len(a)
    for i in range(len(a)):
        if(a[i] >= 0):
            pin = i
            break

    for i in a[pin:]:
        if(i < 0 and dropped >= i and _sum > 0):
            if(rsum < 0):
                _sum -= rsum
            _sum += dropped
            dropped = i
            rsum = _sum + i
        else:
            _sum += i
        if(_sum > maxsum):
            maxsum = _sum
        if(_sum <= 0):
            _sum = 0
            dropped = 0
            rsum = 0

    print(maxsum)
