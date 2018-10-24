T  = int(input())

DATA = [{'N': 0, 'A': []} for i in range(T)]

for i in range(T):
    DATA[i]['N'] = int(input())
    DATA[i]['A'] = [int(i) for i in input().split()]

print(DATA)

for i in range(T):
    remaining = DATA[i]['N'] - 1
    power = DATA[i]['A'][0]

    days = 0
    # iterators
    j = 1 
    while True:
        currentPower = power
        days += 1
        if remaining <= power:
            break

        for k in range(currentPower):
            power += DATA[i]['A'][j+k]
        j += currentPower
        remaining -= currentPower
    print(days)
