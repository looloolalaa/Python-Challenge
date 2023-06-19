# 단어가 포함되는 집합과 포함 안되는 집합
N = int(input())
data = [input() for _ in range(N)]
data.sort()

x_set0 = set()
x_set1 = set()
for d in data:
    # x_set vs x_set+d
    # print(x_set0, x_set1)
    if all(not d.startswith(a) and not a.startswith(d) for a in x_set0):
        x_set0.add(d)


    if all(not d.startswith(a) and not a.startswith(d) for a in x_set1):
        x_set1.add(d)
    else:
        deleted = []
        for a in x_set1:
            if d.startswith(a) or a.startswith(d):
                deleted.append(a)

        for de in deleted:
            x_set1.remove(de)
        x_set1.add(d)


# print(x_set0, x_set1)
print(max(len(x_set0), len(x_set1)))
