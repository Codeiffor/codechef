from functools import lru_cache
import math
T  = int(input())

DATA = [{'N': 0} for i in range(T)]

for i in range(T):
    DATA[i]['N'] = int(input())

@lru_cache(maxsize=10000)
def isPrime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False

    sqrt = int(math.sqrt(n))

    i = 5
    while i<=sqrt:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True 

@lru_cache(maxsize=1000)
def isSemiPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0 and i!=(n//i):
                return isPrime(i) and isPrime(n//i)
    return False

for i in range(T):
    num = DATA[i]['N']
    flag = False

    for i in range(num, num//2-1, -1):
        if isSemiPrime(i) and isSemiPrime(num-i):
            flag = True
            break

    if flag:
        print('YES')
    else:
        print('NO')
