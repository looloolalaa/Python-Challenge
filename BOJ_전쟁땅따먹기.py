from collections import Counter

for _ in range(int(input())):
    line = list(map(int, input().split()))
    n = line[0]
    counter = Counter(line[1:])

    for k, v in counter.items():
        if v > n//2:
            print(k)
            break
    else:
        print('SYJKGW')
