# 축 대칭 후 거리 측정
def solution(m, n, startX, startY, balls):
    def min_d(x, y):
        diagonal = []
        # (0, 0)
        if x[1] / x[0] == y[1] / y[0] and x[0] < y[0]:
            dx = (x[0] ** 2 + x[1] ** 2) ** (0.5)
            dy = (y[0] ** 2 + y[1] ** 2) ** (0.5)
            diagonal.append(round((dx + dy) ** 2))

        # (0, n)
        if (n - x[1]) / x[0] == (n - y[1]) / y[0] and x[0] < y[0]:
            dx = (x[0] ** 2 + (n - x[1]) ** 2) ** (0.5)
            dy = (y[0] ** 2 + (n - y[1]) ** 2) ** (0.5)
            diagonal.append(round((dx + dy) ** 2))

        # (m, 0)
        if x[1] / (m - x[0]) == y[1] / (m - y[0]) and y[0] < x[0]:
            dx = ((m - x[0]) ** 2 + x[1] ** 2) ** (0.5)
            dy = ((m - y[0]) ** 2 + y[1] ** 2) ** (0.5)
            diagonal.append(round((dx + dy) ** 2))

        # (m, n)
        if (n - x[1]) / (m - x[0]) == (n - y[1]) / (m - y[0]) and y[0] < x[0]:
            dx = ((m - x[0]) ** 2 + (n - x[1]) ** 2) ** (0.5)
            dy = ((m - y[0]) ** 2 + (n - y[1]) ** 2) ** (0.5)
            diagonal.append(round((dx + dy) ** 2))

        # print(diagonal)

        left, right, top, bottom = -1, -1, -1, -1
        if x[0] == y[0]:
            if x[1] < y[1]:
                top = float('inf')
                bottom = (x[1] + y[1]) ** 2
            if x[1] > y[1]:
                bottom = float('inf')
                top = ((n - x[1]) + (n - y[1])) ** 2

        else:
            leading, trailing = (x, y) if x[0] < y[0] else (y, x)

            width = trailing[0] - leading[0]
            a = (leading[1] * width) / (trailing[1] + leading[1])
            bottom = round(((a ** 2 + leading[1] ** 2) ** (0.5) + (trailing[1] ** 2 + (width - a) ** 2) ** (0.5)) ** 2)

            a = ((n - leading[1]) * width) / ((n - trailing[1]) + (n - leading[1]))
            top = round(
                ((a ** 2 + (n - leading[1]) ** 2) ** (0.5) + ((n - trailing[1]) ** 2 + (width - a) ** 2) ** (0.5)) ** 2)
            # print(top, bottom)

        if x[1] == y[1]:
            if x[0] < y[0]:
                right = float('inf')
                left = (x[0] + y[0]) ** 2
            if x[0] > y[0]:
                left = float('inf')
                right = ((m - x[0]) + (m - y[0])) ** 2
        else:
            up, down = (x, y) if x[1] > y[1] else (y, x)

            # 3 == up[0], 7 == down[0], 4 == height

            height = up[1] - down[1]
            a = (up[0] * height) / (down[0] + up[0])
            left = round(((a ** 2 + up[0] ** 2) ** (0.5) + (down[0] ** 2 + (height - a) ** 2) ** (0.5)) ** 2)

            a = (m - up[0]) * height / ((m - down[0]) + (m - up[0]))
            right = round(
                ((a ** 2 + (m - up[0]) ** 2) ** (0.5) + ((m - down[0]) ** 2 + (height - a) ** 2) ** (0.5)) ** 2)
            # print(left, right)

        return min([left, right, top, bottom] + diagonal)

    result = []
    for ball in balls:
        re = min_d((startX, startY), ball)
        if re < 0:
            while True:
                pass
        result.append(re)

    # print(min_d((3, 3), (4, 4)))
    # print(min_d((3, 7), (7, 7)))
    # print(round(((a**2 + 3**2)**(0.5) + (7**2 + (4-a)**2)**(0.5)) ** 2))
    return result

# 7/a == 3/(width-a)
# 3a = 7(width-a)
# (3+7)a = 7w
# a = 7w/(3+7)

# a/3 == (4-a)/7

# 7a == 3(4-a)
# 10a == 12

# root(a^2 + 3^2) + root(7^2 + (4-a)^2)
