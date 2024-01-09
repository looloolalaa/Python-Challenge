N = int(input())
j = 0
for i in range(1, 1000_0000):
    if '666' in str(i):
        j += 1
        if j >= N:
            print(i)
            break


