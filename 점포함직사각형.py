point = [[1,2], [0,0], [3,3], [8,9], [7,3], [-10,10]]

x = []
y = []
for p in point:
    x.append(p[0])
    y.append(p[1])

x.sort()
y.sort()
print(x[0], x[-1], y[0], y[-1])